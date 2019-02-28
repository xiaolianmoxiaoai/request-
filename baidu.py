import urllib.request
url = 'https://www.baidu.com/'
response = urllib.request.urlopen(url)
response = response.read()
print(response)