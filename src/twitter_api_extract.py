from datetime import datetime, timedelta
import requests
import json

## URL
TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.00Z"
start_time = (datetime.now() + timedelta(-1)).date().strftime(TIMESTAMP_FORMAT)
end_time = datetime.now().strftime(TIMESTAMP_FORMAT)
query = "data science"

tweet_fields = "tweet.fields=author_id,conversation_id,created_at,id,in_reply_to_user_id,public_metrics,lang,text"
user_fields = "expansions=author_id&user.fields=id,name,username,created_at"


## since Twitter API is paid, I am using this other one that simulates the original one
url_raw = f"https://labdados.com/2/tweets/search/recent?query={query}&{tweet_fields}&{user_fields}&start_time={start_time}&end_time={end_time}"

#PRINTING JSON RESPONSE
response = requests.request("GET", url_raw)
json_response = response.json()
print(json.dumps(json_response, indent=4, sort_keys=True))
