import random
import pyautogui

character = "0123456789abcdefghijklmnopqrstuvwxyz"
character_list = list(character)

# the pyautogui for asking the user for password
password = pyautogui.password('Enter the password here: ')

guess_password = ''  # the variable for the guess password for the user

while guess_password != password:
    guess_password = random.choices(character_list, k=len(password))
    print('>>>' + str(guess_password) + '<<<<')
    if guess_password == list(password):
        pyautogui.confirm('Your Password is : ' + ''.join(guess_password))
        break
