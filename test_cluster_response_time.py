import requests
import pprint as pp
import sys


headers = {
    'Content-Type': 'application/json',
}

data = '{"profile": true,"query" : {"match" : { "ts_date" : "20180315" }}}'

response = requests.post('http://{}:9200/filebeat/_search?human=true'.format(sys.argv[1]), headers=headers, data=data)

pp.pprint(response.json())
