from urllib import request
import json
with request.urlopen('http://v.juhe.cn/weather/index?format=2&cityname=%E8%8B%8F%E5%B7%9E&key=562e96fc4ffae380a0c4e825324fdc1d') as f:
    data = f.read()
    #
    # print('Status:', f.status, f.reason)
    # print('\n\n')
    # for k, v in f.getheaders():
    #     print(k,v)
    # print('\n\n')
    # print('Data:', data.decode('utf-8'))

q = data.decode('utf-8')

parsed_json = json.loads(q)

print(parsed_json['result']['today']['temperature'])