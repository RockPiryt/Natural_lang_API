import os
from dotenv import load_dotenv
import requests
import datetime as dt
from os.path import join, dirname


# Get secrets
# load_dotenv("C:/Users/Popuś/Desktop/Python/environment_variables/.env")
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Nutrition_ix API info
APP_ID_NUTRITION_IX = os.getenv("application_id_nutrition_ix")
API_KEY_NUTRITION_IX = os.getenv("api_key_nutrition_ix")
ENDPOINT_NUTRITION_IX = "https://trackapi.nutritionix.com"
EXERCISE_ENDPOINT = f"{ENDPOINT_NUTRITION_IX}/v2/natural/exercise"

# Sheety info
ENDPOINT_SHEETY = "https://api.sheety.co/25eb7ac5da24422a7caaac1fe67bac5a/workoutTracking/workouts"
BEARER_TOKEN_SHEETY = os.getenv("bearer_token_sheety")
BASIC_AUTH_USERNAME_SHEETY = os.getenv("basic_auth_username_sheety")
BASIC_AUTH_PASSWORD_SHEETY = os.getenv("basic_auth_password_sheety")


# Format date
date = dt.datetime.now().date()#2023-06-26
formatted_date = date.strftime("%d/%m/%Y") #26/06/2023
# Format time
time = dt.datetime.now().time()#19:21:39.509711
formatted_time = time.strftime("%X") #07:06:05

# GENDER = "female"
# WEIGHT = "70.2"
# HEIGHT = "163.5"
# AGE = "33"

user_exercise = input("Tell me which exercise you did: ")
user_gender = input("Tell me your gender: ")
user_weight = float(input("Tell me your weight in kg: "))
user_height = float(input("Tell me your height in cm: "))
user_age = int(input("Tell me your age: "))


headers = {"x-app-id": APP_ID_NUTRITION_IX,
           "x-app-key": API_KEY_NUTRITION_IX,
           }

nutrition_params={
    "query": user_exercise,
    "gender": user_gender,
    "weight_kg" : user_weight,
    "height_cm": user_height,
    "age": user_age,
}

response_nutrition_ix = requests.post(url=EXERCISE_ENDPOINT, 
                        headers=headers, 
                        json=nutrition_params)

result = response_nutrition_ix.json()
#key:list[value1, value2, value3]
# {'exercises': [{'tag_id': 317, 'user_input': 'ran', 'duration_min': 31.08, ....}]}

#----------------------ONE VALUE
# Read one value1 [index=0]
exercise_type = result["exercises"][0]["name"].title()#Bicycling
duration = result["exercises"][0]["duration_min"]#66.67
calories = result["exercises"][0]["nf_calories"]#530.43

sheety_params={
    "workout":{
        "date": formatted_date,
        "time": formatted_time,
        "exercise": exercise_type,
        "duration": duration,
        "calories": calories,
    }
}


# #----------------------FOR LOOP
# # For loop
# exercise_result = result["exercises"]
# #list with dictionaries
# # [{'tag_id': 317, 'user_input': 'ran', 'duration_min': 31.08, 'met': 9.8, 'nf_calories': 356.36, ...}]

# for exercise in exercise_result: 
#     sheety_params={
#         "workout":{
#             "date": formatted_date,
#             "time": formatted_time,
#             "exercise": exercise["name"].title(),
#             "duration": exercise["duration_min"],
#             "calories": exercise["nf_calories"],
#         }
#     }

#Bearer Token Authentication
headers_sheety={
    "Authorization": f"Bearer {BEARER_TOKEN_SHEETY}"
}
response_sheety = requests.post(url=ENDPOINT_SHEETY, 
                                json=sheety_params, 
                                headers=headers_sheety)



# #Basic Authentication
# response_sheety = requests.post(url=ENDPOINT_SHEETY, 
#                                 json=sheety_params, 
#                                 auth=(
#                                     BASIC_AUTH_USERNAME_SHEETY,
#                                     BASIC_AUTH_PASSWORD_SHEETY,
#                                       ))




# print(response_sheety.text)
# {
#   "workout": {
#     "date": "26/06/2023",
#     "time": "19:37:06",
#     "exercise": "Running",
#     "duration": 105.66,
#     "calories": 1211.5,
#     "id": 3
#   }
# }






