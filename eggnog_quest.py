
import time

won = False
said = 0

def lprint(string, delay=0.1):
    time.sleep(0.5)
    things = string.split('\n')
    for x in things:
        print(x)
        time.sleep(delay)
        
def linput(string):
    time.sleep(0.5)
    things = string.split('\n')
    for x in things[:-1]:
        print(x)
        time.sleep(0.1)
    return input(things[-1])

def rollcredits():
    linput("""
                         **** Eggnog Quest IV ****




Programming ........................................................... Sean




Writing ............................................................... Sean




Art Direction ......................................................... Sean




Legal Team ............................................................ Sean




Music ................................................................. Sean




Technical Support ..................................................... Sean




VP of Marketing ....................................................... Sean




Executive Director of Acquisitions .................................... Sean




Colour Distribution Technician ........................................ Sean




Editing by ............................................................ Sean




Additional Editing .................................................... Sean




Production Associate .................................................. Sean




Choreography & Additional FX .......................................... Sean




Senior Chief of Telemarketing ......................................... Sean












                              ***** THE END *****











""")

loadingbar = "[               ]"

for x in range(6): print('\n')

for x in range(16):
    time.sleep(0.15)
    for y in range(6): print('\n')
    loadingbar = loadingbar.replace(' ', "#", 1)
    print(' ' * 32 + loadingbar + '\n' + ' ' * 36 + "loading" + '.' * (x%4))
    for z in range(4): print('\n')


linput("""









                            **** Eggnog Quest IV ****
                            
                     The Phenomenal Text Adventure Experience
                               





                            

                                                                         

Press Enter to continue...                                               v1.00
""")
lprint("""


                                    *******



You are standing in a windy field. The sky is overcast. It's a bit nippy out.

You can see a forest to the north.

There is a fern here.

Your palms are slightly sweaty.

Type "Help" for commands.






""")
curt = 0

while won == False:
    if curt == 1:
        time.sleep(0.1)
        line = input(""">>>""").lower()
    else:line = linput("""
>>>""").lower()
    if line == "help":
        lprint("""
inventory: ......... list inventory

go [N/E/S/W]: ...... move to another location

examine [item]: .... examine an item in your inventory

use [item]: ........ use an item in your inventory

help: .............. show help
""")
    elif line == "inventory":
        lprint("""
You have:

001 x egg
001 x nog
""")
    elif line[:2] == "go":
        said += 1
        if said == 1: lprint("You don't feel like it right now.")
        elif said == 2: lprint("Also, your legs are broken, so there's that.")
        elif said == 3: lprint("No.")
        elif said == 4: curt = 0
        elif said == 5: lprint("No!")
        else: curt = 1
        
    elif line[:8] == "examine ":
        if line[8:] == "egg":
            lprint("It's an egg.")
        elif line[8:] == "nog":
            lprint("It's a nog.")
        else: lprint("Huh?")
    elif line[:4] == "use ":
        if line[4:] == "egg" or line[4:] == "nog":
            useon = linput("What will you use " + line[4:] + " on?: >>>")
            if useon == "egg" and line[4:] == "nog" or useon == "nog":
                lprint("""
 .
 ..
 ...""", 0.5)
                lprint("""

You successfully egg the nog.""")

                linput("""
Congratulations! You have won the game.

Press enter to continue...""")
                rollcredits()
                won = True
            else: lprint("That object is unfit for " + line[4:] + ".")
        else: lprint("You don't have one of those to use.")
    else: lprint("Huh?")
    
