# %%
import json 
import requests 
import pandas as pd

api_token = 'H8BKxyrq5QPhhJamFxGWnzDLrdJAn6aekdYYhgBC'
workspace_id = 'fcdab3cc-e012-4737-bf26-01dfccf65f82'

auth_url = 'https://eu-svc.leanix.net/services/mtm/v1/oauth2/token' 
request_url = 'https://eu-svc.leanix.net/services/mtm/v1/workspaces/%s/users?page=0'%(workspace_id) 

# Get the bearer token - see https://dev.leanix.net/v4.0/docs/authentication
response = requests.post(auth_url, auth=('apitoken', api_token),
                         data={'grant_type': 'client_credentials'})
response.raise_for_status() 
access_token = response.json()['access_token']
auth_header = 'Bearer ' + access_token
header = {'Authorization': auth_header}


# General function to call GraphQL given a query
def call():
  response = requests.get(url=request_url, headers=header)
  response.raise_for_status()
  return response.json()

for user in call()['data']:
  
  print ("First Name:" + " " + user['firstName'] + "\n"  
         "Last Name:" + " " + user['lastName'] + "\n"
         "Email:" + " "   +  user['email'] + "\n" 
         "Status:" + " "   +  user['status'] + "\n"
         "Role:" + " "   +  user['role'] + "\n" ) # +
         # char(user["lastLogin"]) )
         