# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 11:45:23 2019

@author: PG
"""

import random

list = [1, 2, 3, 4, 5, 6];
#max(list)
#min(list)

def roll_dice():
    m = random.choice(list)
    print("Dice rolled , your value - " + str(m))
    
def ask_human():
    text = input("Roll dice again? Y/N : ")
    if text.lower() == "y" or text.lower() == "yes" :
        print("You entered :" +  text)
        roll_dice()
    elif text.lower() == "n" or text.lower() == "no":
        print("No dice for you")
    else:
        print("Y/N are the only valid options moron , you typed - "+ text)
        ask_human()

roll_dice()
ask_human()