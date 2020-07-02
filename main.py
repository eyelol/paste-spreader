import requests
import json
from bs4 import BeautifulSoup

f = open(input("Filename > "))
dox = f.read()

def hastebin():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.8) Gecko/20100101 Firefox/60.8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Content-Type': 'application/json; charset=utf-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://hastebin.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://hastebin.com/',
        'TE': 'Trailers',
    }

    data = dox

    response = requests.post('https://hastebin.com/documents', headers=headers, data=data)
    jsondata = json.loads(response.text)
    print("https://hastebin.com/" + str(jsondata['key']))

def pipfi():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.8) Gecko/20100101 Firefox/60.8',
        'Accept': '*/*',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://p.ip.fi',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://p.ip.fi/',
        'TE': 'Trailers',
    }

    data = {
    'paste': dox
    }

    response = requests.post('https://p.ip.fi/', headers=headers, data=data)
    print(response.text)

def scratchbook():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.8) Gecko/20100101 Firefox/60.8',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://paste.scratchbook.ch',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://paste.scratchbook.ch/',
        'Upgrade-Insecure-Requests': '1',
        'TE': 'Trailers',
    }

    data = {
    'name': '',
    'title': '',
    'lang': 'text',
    'code': dox,
    'expire': '0',
    'email': '',
    'url': '',
    'submit': 'submit'
    }

    response = requests.post('https://paste.scratchbook.ch/', headers=headers, data=data)
    print(response.url)

def hatebin():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.8) Gecko/20100101 Firefox/60.8',
        'Accept': '*/*',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Content-type': 'application/x-www-form-urlencoded',
        'Origin': 'https://hatebin.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://hatebin.com/',
    }

    data = {
    'text': dox
    }

    response = requests.post('https://hatebin.com/index.php', headers=headers, data=data)
    text = response.text
    key = text.strip()
    print("https://hatebin.com/" + key)

def ctxt():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.8) Gecko/20100101 Firefox/60.8',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://ctxt.io',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://ctxt.io/',
        'Upgrade-Insecure-Requests': '1',
        'TE': 'Trailers',
    }

    data = {
    'content': dox,
    'ttl': '1d'
    }

    response = requests.post('https://ctxt.io/new', headers=headers, data=data)
    print(response.url)

def writeas():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.8) Gecko/20100101 Firefox/60.8',
        'Accept': '*/*',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Content-type': 'application/json',
        'Origin': 'https://write.as',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://write.as/new',
    }

    data = {
        'body':dox,
        'font':'norm',
        'lang':'en',
        'crosspost':[],
        'public':False
    }

    response = requests.post('https://write.as/api/posts', headers=headers, json=data)
    jsondata = json.loads(response.text)
    print("https://write.as/" + str(jsondata['data']['id']))

def commie():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.8) Gecko/20100101 Firefox/60.8',
        'Accept': '*/*',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://commie.io',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://commie.io/',
    }

    data = {
    'do': 'save',
    'content': dox
    }

    response = requests.post('https://commie.io/lib/router.php', headers=headers, data=data)
    data = response.text
    data = data.strip('"')
    print("https://commie.io/#" + data)

def paste2():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.8) Gecko/20100101 Firefox/60.8',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://paste2.org',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://paste2.org/',
        'Upgrade-Insecure-Requests': '1',
        'TE': 'Trailers',
    }

    data = {
    'code': dox,
    'lang': 'text',
    'description': '',
    'parent': ''
    }

    response = requests.post('https://paste2.org/', headers=headers, data=data)
    print(response.url)


hastebin()
pipfi()
scratchbook()
hatebin()
ctxt()
writeas()
commie()
paste2()