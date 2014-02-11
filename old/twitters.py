# -*- coding: utf-8 -*-
import urllib2
#from BeautifulSoup import BeautifulSoup
import sys
import re
import json
import csv
from transliterate.utils import translit

df_pos=open('fon_pos.txt', 'r')
df_neg=open('fon_neg.txt', 'r')
tf=open('tweets.csv','r')
#aaf=open('msk_realty_add.csv','w')
f = open('all_tweets', 'w')

#print hf.read()
#homes = csv.reader(hf.read().split('\n'), delimiter=';')
homes=hf.read().split('\n')
addresses=af.read().split('\n')

addr={}
for row in addresses:
	a=row.split(';')
	addr[a[0]]={}
	addr[a[0]]['addr']=a[2]+', '+a[1]
	addr[a[0]]['area']=a[3]
	print a[0]+addr[a[0]]['addr']

hf.close()
f.close()
#aaf.close()