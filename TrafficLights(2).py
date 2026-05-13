from microbit import *
import radio

init = False

radio.on()
radio.config(group=17)
display.clear()

cross = (Image( '90009:'
                '09090:'
                '00900:'
                '09090:'
                '90009'))

diamond = (Image( '00900'
                  '09990'
                  '90909'
                  '09990'
                  '00900'))

complete_diamond = (Image( '00900'
                          '09990'
                          '99999'
                          '09990'
                          '00900'))

def feu_rouge():
    for i in range(5,-1,-1):
        """affiche le décompte du feu"""
        display.show(cross)
        sleep(1000)
        display.show(i)
        sleep(1000)


def feu_vert():
    for _ in range(9):
         sleep(1000)
         display.show(Image.ARROW_N)
    sleep(1000)
    display.show(diamond)
    sleep(1000)
    display.show(complete_diamond)


init = True


while True:
    if button_a.is_pressed(): 
        while True:
            radio.send("init")
            sleep(10)
            feu_rouge()
            feu_vert()
