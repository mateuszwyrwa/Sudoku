import numpy as np
from Creating import *

all = {1,2,3,4,5,6,7,8,9}


def vertical(x): #creates collection of vertical numbers from point
    virt = t[x]
    return virt

def horizontal(y):
    virt = t[:,y]
    return virt


def whichsquare(x,y): #check in which square program is and creates list of numbers
    if x <= 2:
        if y <= 0:
            sqre = [t[:3,0:3]]
        if y <= 5 and y > 2:
            sqre = [t[3:6,0:3]]
        if y > 5:
            sqre = [t[6:,0:3]]
    elif x <= 5 and x>2:
        if y <= 0:
            sqre = [t[:3,3:6]]
        if y <= 5 and y > 2:
            sqre = [t[3:6,3:6]]
        if y > 5:
            sqre = [t[6:,3:6]]
    elif x > 5:
        if y <= 0:
            sqre = [t[:3,6:]]
        if y <= 5 and y > 2:
            sqre = [t[3:6,6:]]
        if y > 5:
            sqre = [t[6:,6:]]
    return sqre



for x in range(9):
    something = whichsquare(x,0)
    print(something)
