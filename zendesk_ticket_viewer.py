from dotenv import load_dotenv
import os

import requests
import json
import sys
import subprocess

load_dotenv('.env')
# Set the request parameters
url = 'https://zcczmckenzie.zendesk.com/api/v2/tickets.json'
user = 'zmckenzie82@gmail.com' # + '/token:'
pwd = os.getenv('ZENDESK_PWD')# 'g634iwJ6FBodcZ6cQswRHKbLsCqGSnYeIs4tDXSe!'

# Do the HTTP get request
response = requests.get(url, auth=(user, pwd))

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
temp = json.dumps(data, indent=4)

# print('Total tickets: ', data['count'])
print(temp, '\n')

while True:
    print('To see all tickets again, type "all".')

    user_input = input('Enter a number between 0 - 21: ')

    if user_input.isdigit():
        user_input = int(user_input)
        if user_input > 21:
            print("Sorry, no ticket exists of that number: ", user_input)
        else:
            print('You inputted for ticket id:', user_input, '\nassignee_id:', data['tickets'][user_input]['assignee_id'],
                '\nsubject:', data['tickets'][user_input]['subject'], '\ndescription:', data['tickets'][user_input]['description'],
                '\nstatus:', data['tickets'][user_input]['status'], '\n')
    elif user_input == 'all':
        user_input.lower()
        print(temp)
    else:
        print('Sorry, that does not qualify as a number. Try again!')

if __name__ == '__main__':
    if '--unittest' in sys.argv:
        subprocess.call([sys.executable, '-m', 'unittest', 'zendesk_ticket_viewer.py'])
