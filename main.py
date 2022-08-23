from datetime import date, datetime,timedelta
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random

#today = datetime.now()+timedelta(hours=8)
start_date = os.environ['START_DATE']
city = os.environ['CITY']
birthday = os.environ['BIRTHDAY']

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_id = os.environ["USER_ID"]
template_id = os.environ["TEMPLATE_ID"]


today = date.today()  #获取今天的日期
my_birthday = birthday
if my_birthday < today:#如果你今年的生日过了，加到下一年
    my_birthday = my.replace(year=today.year+1)
time_to_birthday = abs(my - today) #算一下这两天差了多少时间戳
print(time_to_birthday.days)
