#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import sys, getopt

def login():
	url = 'https://w.seu.edu.cn/index.php/index/login'
	post_data = {'username':'your id', 'password':'password in base64', 'enablemacauth':0}
	request = Request(url, urlencode(post_data).encode())
	json = urlopen(request).read().decode('unicode-escape')
	print(json)

def logout():
	url = 'http://w.seu.edu.cn/index.php/index/logout'
	request = Request(url, urlencode({}).encode())
	json = urlopen(request).read().decode('unicode-escape')
	print(json)

if __name__ == "__main__":
	argv = sys.argv
	if argv[1] == '-i':
		login()
	elif argv[1] == '-o':
		logout()
	else:
		print('Wrong option. -i or -o ?')
