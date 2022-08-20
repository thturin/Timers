import pygame, sys
from random import randint


pygame.init() #starts the timer
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

current_time = 0 #measure time at every frame
button_press_time = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN: #checks if any button has been pressed down
            button_press_time = pygame.time.get_ticks()
            screen.fill('white')

    current_time = pygame.time.get_ticks() #what time we have ms riugut now
    #print(current_time) #the difference between each tick/frame is around 16 which is 1000/60
    print('current time: {} button press time: {}'.format(current_time,button_press_time))

    timer = current_time-button_press_time
    if timer > 2000: #if the timer reaches 2 seconds
        screen.fill('blue')

    pygame.display.flip()
    clock.tick(60)