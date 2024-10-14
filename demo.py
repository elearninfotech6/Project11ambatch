import requests
import json

res=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
d=res.json()
print(d['time']['updatedISO'])
print(d['bpi']['USD']['rate'])
