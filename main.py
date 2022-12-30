import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

headers = {
    "x-app-id": os.getenv("APP_ID"),
    "x-app-key": os.getenv("API_KEY"),
    "Content-Type": "application/json",
    "Authorization": os.getenv("SHEETY_AUTHORIZATION")
}

query = input("Tell me which exercises you did: ")

post_params = {
    "query": query
}

response = requests.post(url=os.getenv("EXERCISE_END_POINT"),
                         json=post_params, headers=headers)
data = response.json()

print(data)

for exercise in data["exercises"]:

    date = datetime.now()

    sheet_params = {
        "workout": {
            "date": date.strftime("%d/%m/%Y"),
            "time": date.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(
        url=os.getenv("SHEETY_POST_URL"), json=sheet_params, headers=headers)
    print(sheety_response.text)
