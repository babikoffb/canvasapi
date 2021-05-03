# Boilerplate code from the documentation
# Import the Canvas class
from canvasapi import Canvas

# Canvas API URL
API_URL = ""
# Canvas API key
API_KEY = ""

#This is something that should be hard coded for testing
account_number = ""

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

def create_new_user():
    # Grab the account to create the user under
    account = canvas.get_account(account_number)

    username = input("Enter username: ")
    new_user_pass = input("Enter new user's password: ")
    new_user_sis_id = input("Enter new user's SIS ID number: ")

    user = account.create_user(
        user={
            'name': username
        },
        pseudonym={
            'password': new_user_pass,
            'sis_user_id': new_user_sis_id
        }
    )

def edit_user():

    username = input("Enter user Canvas ID: ")
    new_username = input("Enter new username: ")
    user = canvas.get_user(username)

    user.edit(
        user={'name': new_username}
    )