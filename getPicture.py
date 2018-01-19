import re
import requests
import os

# 判定该目录是否存在，假如不存在则创建
"""def get_backphoto(path):
   if (os.path.exists(path)== False):
        os.mkdir(path)"""


# 根据关键字爬取相关图片
def download_pic(keyword, path):
    n = 10
    for i in range(n):
        tem = str(i * 60)
        url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + keyword + '&pn=' + tem + '&gsm=0'
        html = requests.get(url).text
        html = html.decode("utf-8");
        pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
        n = i * 60
        for each in pic_url:
            print(each)
            try:
                pic = requests.get(each, timeout=80)
            except requests.exceptions.ConnectionError:
                print('该照片无法下载')
                continue
            if (os.path.exists(path) == False):
                os.mkdir(path)
                string = path + keyword + str(n) + '.jpg'
            else:
                string = path + keyword + str(n) + '.jpg'
            fp = open(string, 'wb')
            fp.write(pic.content)
            fp.close()
            n = n + 1


keyword = input("请输入关键字(eg:小黄人) : ");
path = input("请输入路径(eg:D:/images/小黄人/)  :")
download_pic(keyword, path)
