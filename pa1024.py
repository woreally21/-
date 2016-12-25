,''##coding:utf-8##
import requests
from bs4 import BeautifulSoup
import lxml
import re
'''
批量爬取1204贴图区帖子名
1024导航网站http://1024bug.me/
'''
baseurl = 'http://xiaohai.ga/'
result = []

def getsoup(URL):
    req= requests.get(URL)
    req.encoding = 'gbk'  ##这玩意的编码要自己定！！！！否则它就随便弄一个
    soup = BeautifulSoup(req.text,'lxml')
    return soup

def wr(baseurl):
    page=raw_input('爬多少页')
    for i in range(1,int(page)+1):
        url_page = baseurl + 'thread0806.php?fid=16&amp;search=&amp;page=' + str(i)
        print url_page
        soup = getsoup(url_page)
        cache = soup.find_all(text = re.compile('P]'))
        print type(cache)
        for i in range(len(cache)):
            result.append(cache[i])
        print len(cache)

print '开车'
txt = open('1.txt','w')
wr(baseurl)
for i in range(len(result)):
    txt.write(str(result[i].encode('utf-8')))
    txt.write('\n')
txt.close()


##问题：  匹配的数目不够（line25 正则匹配问题）
        
        
    
    
