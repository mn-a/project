import requests
import json
import logging

URL = "https://m.land.naver.com/map/35.9017473:128.8470917:14:4729025300/OR/B2#mapFullList"

param = {
    'view': 'atc1',
    'cortarNo' : '4729025300'
    'rletipCd' : 'OR'
    'tradTpCd': 'B2',
    'order': 'date_',
    'showR0': 'N',
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
    'Referer': 'https://m.land.naver.com/'
}

logging.basicConfig(level=logging.INFO)
page = 0

while True:
    page += 1
    param['page'] = page

    resp = requests.get(URL, params=param, headers=header)
    if resp.status_code != 200:
        logging.error('invalid status: %d' % resp.status_code)
        break

    data = json.loads(resp.text)
    result = data['result']
    if result is None:
        logging.error('no result')
        break
    
    for item in result['list']:
        if float(item['spc2']) < 80 or float(item['spc2']) > 85:
            continue
        logging.info('[%s] %s %s층 %s만원' % (item['tradTpNm'], item['bildNm'], item['flrInfo'], item['prcInfo']))
    
    if result['moreDataYn'] == 'N':
        break

