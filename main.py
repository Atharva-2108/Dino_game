# import pyautogui  # pip install pyautogui
# from PIL import Image, ImageGrab  # pip install pillow
# import time


# def pressKey(key):
#     pyautogui.keyDown(key)


# def isCollision(data):
#     for i in range(200, 250):
#         for j in range(550, 680):
#             if data[i, j] < 100:
#                 pressKey('up')
                



# def takeScreenshot():
#     image = ImageGrab.grab().convert('L')
#     return image


# if __name__ == "__main__":
#     print("Dino game starts in 3 seconds!")
#     time.sleep(3)
#     # (pressKey'up')
#     while True:
#         image = takeScreenshot()
#         data = image.load()
#         isCollision(data)
#     # for i in range(200, 250):
#     #     for j in range(550, 680):
#     #         data[i, j] = 0

#     # image.show()

import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time

def hit(key):
    pyautogui.press(key)
    return

def isCollide(data):
    # Draw the rectangle for birds
    for i in range(190, 270):
        for j in range(553, 660):
            print(data[190, 553])
            if data[190, 553] < 100:
                hit("down")
                return
               

    for i in range(190, 270):
        for j in range(553, 660):
            print(data[i, j])
            if data[i, j] > 100:
                print('hello')
                hit('up')
                return
    return
                
  
                 
    

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    # hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        # image.show()
        isCollide(data)
            
        # print(asarray(image))
        
        # # Draw the rectangle for cactus
        # for i in range(210, 300):
        #     for j in range(553, 680):
        #         data[i, j] = 0
        
        # # Draw the rectangle for birds
        # for i in range(210, 300):
        #     for j in range(390, 553):
        #         data[i, j] = 171

        # image.show()
        # break
      

