import json
from urllib import request

json_url = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
page = request.urlopen(json_url).read().decode('utf-8')
json_obj = json.loads(page)

base_url = 'https://www.bing.com'
img_url = base_url + json_obj['images'][0]['url'].strip().split('&')[0]

img_title = json_obj['images'][0]['title'].strip().lower().replace(' ', '_')
img_date = json_obj['images'][0]['startdate'].strip()
img_filename = img_date + '_' + img_title + '.jpg'

request.urlretrieve(img_url, filename=img_filename)
