import requests
from datetime import datetime
import re


# 获得日落时间
def getSunsetTime():
    # 获得格式化过的date
    date = formatTime()
    # 开始获得
    sunset_url = 'https://devapi.qweather.com/v7/astronomy/sunmoon?'
    params = {
        'location': '101280101',
        'key': '6dee7771746148fbbee9cedeb9c1ffc4',
        'date': date,
        'gzip': 'y'
    }
    sun_html = requests.get(sunset_url, params)
    sun_content = sun_html.json()
    sunset_time = sun_content['sunset']
    print('sunset_time:', sunset_time)
    print('sunset_time is: ', type(sunset_time))
    return sunset_time


def formatTime():
    dt = datetime.now()
    year = dt.year
    month = dt.month
    day = dt.day
    today = str(year) + str(month) + str(day)
    # print(today)
    return today


# 分离日落时间，获得几点几分
def getSunsetHM():
    # 使用正则表达式
    sunsetime = getSunsetTime()
    sunsetHM = (re.findall(r"T(.+?)\+", sunsetime))
    print(sunsetHM)
    return sunsetHM


if __name__ == '__main__':
    getSunsetTime()
    getSunsetHM()