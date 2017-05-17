import bs4 as bs
import urllib.request
from string import Template
import sys
import time

sauce = urllib.request.urlopen('http://www.bbc.com/news/popular/read').read()
#sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
#sauce = urllib.request.urlopen('http://edition.cnn.com/specials/last-50-stories').read()
soup = bs.BeautifulSoup(sauce,'lxml')

output = []
for li in soup.find_all('li',class_='most-popular-list-item'):
      ##print (li)
      data = {}
      data['link']=li.a['href']
      output.append(data)
      print (data['link'])

for data in output:
      sauce2 = urllib.request.urlopen('http://www.bbc.com'+data['link']).read()
