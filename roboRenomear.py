import pyautogui
from time import sleep

pyautogui.keyDown('alt')
pyautogui.press(['tab'])
pyautogui.keyUp('alt')
sleep(1)

for c in range(1,11):
    pyautogui.press('f2')
    pyautogui.write('Projeto 0{}'.format(c))
    pyautogui.press('enter')
    sleep(0.3)
    pyautogui.press('home')
    


#372,239