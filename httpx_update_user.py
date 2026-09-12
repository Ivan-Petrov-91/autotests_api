import httpx

from tools.fakers import get_random_email


create_user_payload = {
  "email": get_random_email(),
  "password": "Wire",
  "lastName": "Moreland",
  "firstName": "William",
  "middleName": "Bunk"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}

login_response = httpx.post(
    "http://localhost:8000/api/v1/authentication/login",
    json=login_payload
)
login_response_data = login_response.json()

update_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

update_user_payload = {
  "email": get_random_email(),
  "lastName": "Moreland",
  "firstName": "Will",
  "middleName": "Bunk"
}

update_user_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",
    headers=update_user_headers,
    json=update_user_payload
)
