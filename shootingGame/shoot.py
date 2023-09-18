#Shoot the fruits

#_____________________________________________________________________________
# 'WHEN' the game starts , an Apple appears on the screen for you to "shoot."
# 'IF' you hit it, a ("Good shot!") message pops up,
# 'AND' the applle appears at another('random') point on the screen.
# 'BUT' if you miss, a ("You missed!") message is shown,
# and the gmae 'ends'.
#____________________________________________________________________________

import pgzrun
import pygame
import sys
import os
from random import randint

fruits=["apple", "orange", "pineapple"]
index = 0
for each in fruits:  
    apple=Actor(fruits[index])
    index=randint(0,2)

score = 0
# score_increment = 1


def draw():
    screen.clear()
    apple.draw()
    # apple.draw()

def draw_text():
    screen.draw.text("Good Shot!", topleft=(30, 30))

def count():
    score
    # score += score_increment
    print(score)


    
def place_apple():
    apple.x = randint(10, 300)
    apple.y = randint(10, 300)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good Shot!")
        score+1
        
        
       
        count()
        draw_text()
        place_apple()
        
    else:
        print("You missed!")
        quit()
# total=count()
# print.count(total)
place_apple()
pgzrun.go()