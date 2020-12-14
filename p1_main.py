'''
P1 - Quiz Sysytem

course = CS384-Pyhton
Instructor = Mr. Mayank Agarwal

Group Members:
1. Aparsh Gupta(1801EE08)
2. Khushi Gour(1801CB14) 

Libraries used:
1. Bcrypt
2. Tkinter
3. Threading
4. pynput
5. csv 
6. os
7. pathlib
8. re
9. shutil

Demo Video - https://www.youtube.com/watch?v=tuq4OBdbygA

'''

import database.display_util as display
import database.db as db
import utilities.timer as timer
import fileOperations.read as reader
import threading
import fileOperations.takeQuiz as takeQuiz
from pynput import keyboard

current = set()
# The key combination to check
COMBINATIONS = [
    {keyboard.Key.alt, keyboard.Key.ctrl,keyboard.KeyCode(char='e')}
]

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            db.exportMarksToCsv()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

def hotkeys_export():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

export_thread = threading.Thread(target=hotkeys_export)
export_thread.start()

display.main_account_screen()


'''
tesing account:

username : 1801ee08
password : password123

'''

