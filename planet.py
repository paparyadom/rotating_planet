import time
from sys import platform, argv

from planets_view import earth

try:
    speed = float(argv[1])
except (IndexError, ValueError):
    speed = 1


def win_view(views: str, speed: float):
    import os
    try:
        while True:
            for view in views:
                os.system('cls')
                print(view)
                time.sleep(speed / 100)
    except KeyboardInterrupt:
        print('***STOP***')


def lin_mac_view(views: str, speed: float):
    try:
        while True:
            for view in views:
                print('\033[2J')
                print(view)
                time.sleep(speed / 100)
    except KeyboardInterrupt:
        print('***STOP***')


lin_mac_view(earth, speed) if platform in ('linux', 'darwin') else win_view(earth, speed)
