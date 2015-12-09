import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'http://example.com/')
print('status: ', r.status)
r.headers['server']
print('data: ', r.data)

