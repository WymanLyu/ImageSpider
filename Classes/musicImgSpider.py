
#coding=utf-8

import requests
from json import loads
from bs4 import BeautifulSoup
import re
import multiprocessing as mp
import os
import sys

import requests

def loadImg(keyWord, perPage, page):
    # url
    targetUrl = "https://unsplash.com/napi/search/photos?query=%s&xp=search-deep:excluded,search-extended:excluded,search-story:excluded&per_page=%d&page=%d"\
                % (keyWord, perPage, page)
    # 头部信息
    headers = {'authorization': 'Client-ID d69927c7ea5c770fa2ce9a2f1e3589bd896454f7068f689d8e41a25b54fa6042'}
    # 响应体
    response = requests.get(targetUrl, headers=headers)
    # 转json字典
    rDict = loads(response.text)
    print(rDict)
    # 解析json
    index = 1
    for i in rDict["results"]:
        imgUrl = i["urls"]["full"]
        # response = requests.get(imgUrl)
        if response.status_code == 200:
            with open("%s/%s_img_url_list.txt" %(keyWord,keyWord), "a") as f: # open("%s_img_%d.jpg" %{keyWord, index}, "w")
                f.write(imgUrl)
                f.write("\n")
        index = index + 1
        # 打印链接
        print(i["urls"]["full"])


def main(keyWord):
    # 总页码
    perPage = 20
    # 第一次请求 获取总页数
    firstUrl = "https://unsplash.com/napi/search/photos?query=%s&xp=search-deep:excluded,search-extended:excluded,search-story:excluded&per_page=%d&page=%d" % (
        keyWord, perPage, 1)
    # 头部信息
    headers = {'authorization': 'Client-ID d69927c7ea5c770fa2ce9a2f1e3589bd896454f7068f689d8e41a25b54fa6042'}
    # 响应体
    response = requests.get(firstUrl, headers=headers)
    # 转json字典
    rDict = loads(response.text)
    # 总页数
    totalPage = rDict['total_pages']

    # 创建文件夹
    os.mkdir(keyWord)

    # 循环下载图片
    for i in range(1, totalPage):
        loadImg(keyWord, perPage, i)


if __name__=="__main__":
    # 关键词
    keyWord = ""
    try:
        keyWord = sys.argv[1]
    except Exception:
        print("need a keyword!")
    print("keyword:"+keyWord)
    main(keyWord)



'''
response = requests.get(url='https://unsplash.com/search/music')

print(response.text)

解析第一页的html
soup = BeautifulSoup(response.text, "lxml")
nodes = soup.select('#gridMulti a[style*=""]')

print(nodes[0]['href'])

str = re.search(r'\=.*', nodes[0]['href']).group()
url2 = "https://unsplash.com/photos/" + str[1:]
print('----'+url2)
'''

'''
 解析第二页
 # response2 = requests.get(url=url2)
# soup2 = BeautifulSoup(response2.text, "lxml")
# nodes2 = soup2.select('.RN0KT img[role="presentation"]') #[role="presentation"]
# print(nodes2)
# imgStr = nodes2[0]['src']
# print(imgStr)

# for i in xrange(1,10):
# 	pass
 
 '''





# print(r.text)

