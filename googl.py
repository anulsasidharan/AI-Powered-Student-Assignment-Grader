import requests

url = "https://www.googleapis.com/customsearch/v1"
params = {
    "key": "AIzaSyCTxaIW3pn7arF8XlpuVjjN9F_ZuqP7Lmw" ,
    "cx": "377ea0812fa5e47de",
    "q": "Model Context Protocol MCP"
}

response = requests.get(url, params=params)
print(response.json())
