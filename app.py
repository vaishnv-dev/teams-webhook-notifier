import requests
import json

# Replace with your Teams Webhook URL
url = "YOUR_WEBHOOK_URL"

message = {
    "text": "Hello from GitHub! 🚀 This is a Teams notification."
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, data=json.dumps(message))

print(response.status_code)
