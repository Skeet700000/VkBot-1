import time
import vk_api
import const
import safygiphy
import random
import requests
import pandas
import json

tables = pandas.read_html('https://www.fxclub.org/markets/forex/usd-rub/', header=0)
tables[0].to_json('money.json')

vk_session = vk_api.VkApi(token=const.api_token)
g = safygiphy.Giphy()

with open('C:/Users/Dmitry/Desktop/vkbot/money.json', 'r', encoding='utf-8') as response:
    source = response.read()

data = json.loads(source)
print(data)
# print (data0])

values = {'out': 0,'count': 100,'time_offset': 60}
response = vk_session.method('messages.get', values)

def write_msg(user_id, s):
    vk_session.method('messages.send', {'user_id':user_id,'message':s})

while True:
    response = vk_session.method('messages.get', values)
    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
    for item in response['items']:
            if response['items'][0]['body'] == 'Привет':
                write_msg(item['user_id'], 'И тебе привет')
            if response['items'][0]['body'] == 'Доллар':
                write_msg(item['user_id'], data)
    time.sleep(1)