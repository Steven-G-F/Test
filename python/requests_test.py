import requests

ms_url = "https://www.microsoft.com/en-us/download/confirmation.aspx?id=56519"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

### Download Content of Current URL ###
response = requests.get(ms_url, headers=headers)
html_raw = response.text

### Get Current URL ###
for links in html_raw.split('href='):
    if "ServiceTags_Public_" in links and ".json" in links:
        current_url = links.split('"')[1]

### Get JSON Data from Current URL ###
service_tags_json = requests.get(current_url, headers=headers).json()

print(service_tags_json)
