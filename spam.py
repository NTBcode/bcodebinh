import pyautogui
from pynput.keyboard import Controller
import time
import random


textinput = input("Nhập chữ muốn spam:")
text = textinput.split(", ")
index = 0
end = int(input("nhập số lần cần spam:"))
delay = float(input("Nhập độ delay:"))
time.sleep(10)


while(index < end):
	keyboard = Controller()
	n = random.choice(text)
	keyboard.type(n)
	pyautogui.typewrite("\n")
	time.sleep(delay)
	index += 1