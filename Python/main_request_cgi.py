import requests

#url='http://192.168.15.32:80/cgi-bin/snapshot.cgi?chn=3'
#url='http://192.168.15.32:80/cgi-bin/snapshot.cgi?channel=2&subtype=1'
url='http://admin:gomes20llg@192.168.15.32:80/cgi-bin/snapshot.cgi?channel=3&subtype=1'

user='admin'
password='gomes20llg'
file = open("picture.jpg", 'wb')

credentials = requests.auth.HTTPDigestAuth(user, password)

with requests.get(url, auth=credentials, stream=True) as response:
    for chunk in response.iter_content(chunk_size=128):
        file.write(chunk)

file.close()