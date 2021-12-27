import pyautogui
import logging
import datetime
import time
import random
import sys

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
random.seed()


def getScreenCenter():
    screenX, screenY = pyautogui.size()
    logging.debug(f"X: {screenX} Y: {screenY}")
    return screenX/2, screenY/2


def getDesiredClickTimeSeconds():
    desiredTime = input("How many minutes to click? [30]")
    if desiredTime == None:
        desiredTime = 30
    else:
        desiredTime = int(desiredTime)
    return desiredTime * 60


def randomSleep():
    return random.randint(10, 70) / 100


desiredTimeSeconds = getDesiredClickTimeSeconds()

print(
    f"Sleeping 5 seconds and clicking for {desiredTimeSeconds} seconds; get ready.")
time.sleep(5)

timeout = int(time.time()) + desiredTimeSeconds
while time.time() < timeout:
    logging.debug(f"{time.time()} < {timeout}")
    pyautogui.click(1200, 1200)
    clickSleep = randomSleep()
    logging.debug(f"Sleeping between click: {clickSleep}")
    time.sleep(clickSleep)

sys.exit()
