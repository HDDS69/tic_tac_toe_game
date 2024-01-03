# -*- coding: utf-8 -*-
import pygame
import sys
import time
import random

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("tick-tack-toe")
#колизия кнопок
win = pygame.display.set_mode((550, 600))
win_game = pygame.Rect(160, 190, 261, 284)
button_rect = pygame.Rect(180, 270, 200, 50)
button_rect1 = pygame.Rect(180, 370, 200, 50)

pointcolision = (pygame.Rect(164, 210, 84, 100),pygame.Rect(250, 210, 90, 90),pygame.Rect(340, 210, 100, 90),pygame.Rect(170, 300, 80, 90),pygame.Rect(250, 300, 90, 100),
                pygame.Rect(340, 300, 100, 100),pygame.Rect(164, 390, 84, 100),pygame.Rect(250, 390, 90, 100),pygame.Rect(340, 390, 100, 100))
#импорт текстур / звуков / шрифтов
bg = pygame.image.load("texture/bg.jpg")
listbg = pygame.image.load("texture/pole.png")
x = pygame.image.load("texture/x.png")
o = pygame.image.load("texture/o.png")
FAnt = pygame.font.Font('texture/font.ttf', 30)
hit = pygame.mixer.Sound("texture/hit.mp3")
#функция кнопки
def button():
  win.blit(bg, (0, 0))
  button_color = (217, 145, 78)
  text = FAnt.render('play',False, (0, 0, 0))
  text1 = FAnt.render('play vs bot',False, (0, 0, 0))
  text2 = FAnt.render('tick-tack-toe',False, (255, 255, 255))
  text_rect = text.get_rect(center=button_rect.center)
  pygame.draw.rect(win, button_color, button_rect)
  pygame.draw.rect(win, button_color, button_rect1)
  win.blit(text, text_rect)
  win.blit(text1, (200, 375))
  win.blit(text2, (200, 150))
  pygame.display.update()
#функция отрисовки поля
def animated(name):
    win.blit(bg, (0, 0))
    win.blit(listbg, (100, 150))
    text = FAnt.render(name, True, (255, 255, 255))
    win.blit(text,(175,0))
    if point[0] == 1:
        win.blit(cells[0],(164,210))
    if point[1] == 1 :
        win.blit(cells[1],(250,210))
    if point[2] == 1 :
        win.blit(cells[2],(340,210))
    if point[3] == 1 :
        win.blit(cells[3],(170,300))
    if point[4] == 1 :
        win.blit(cells[4],(250,300))
    if point[5] == 1 :
        win.blit(cells[5],(340,300))
    if point[6] == 1 :
        win.blit(cells[6],(164,390))
    if point[7] == 1 :
        win.blit(cells[7],(250,390))
    if point[8] == 1 :
        win.blit(cells[8],(340,390))
    pygame.display.update()
#функция проверки выйгрыша
def check():
    if (cells[0] == cells[1] == cells[2] == x) or (cells[3] == cells[4] == cells[5] == x) or (cells[6] == cells[7] == cells[8] == x) :
        return 2
    elif (cells[0] == cells[3] == cells[6] == x) or (cells[1] == cells[4] == cells[7] == x ) or (cells[2] == cells[5] == cells[8] == x) :
        return 2
    elif (cells[0] == cells[4] == cells[8] == x) or (cells[2] == cells[4] == cells[6] == x):
        return 2
    elif (cells[0] == cells[1] == cells[2] == o) or (cells[3] == cells[4] == cells[5] == o) or (cells[6] == cells[7] == cells[8] == o ) :
        return 0
    elif (cells[0] == cells[3] == cells[6] == o) or (cells[1] == cells[4] == cells[7] == o ) or (cells[2] == cells[5] == cells[8] == o) :
        return 0
    elif (cells[0] == cells[4] == cells[8] == o) or (cells[2] == cells[4] == cells[6] == o) :
        return 0
    elif point[0] == point[1] == point[2] == point[3] == point[4] == point[5] == point[6] == point[7] == point[8] == 1:
        return 1
#функция перехода игрока
def x_o(c):
    global current_player,cells,point,xexe
    point[c] = 1
    if current_player == 0:
        current_player += 1
        cells[c] = x
        xexe = c      
    else:
        current_player = 0
        cells[c] = o
        
def playermove():
    if event.type == pygame.MOUSEBUTTONDOWN:
      if win_game.collidepoint(event.pos):
       for i in range(9):
        if pointcolision[i].collidepoint(event.pos) and point[i] == 0:
              hit.play()
              x_o(i)
              
def esle():
 for i in range(9):
    if point[i] == 0:
        x_o(i)
        break
#основной цикл игры
while True:
 name = ""
 cells = [0,1,2,3,4,5,6,7,8]
 point = [0,0,0,0,0,0,0,0,0]
 current_player = 0
 xexe = None
 game = 0
 run = True
 while run:
    button()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if button_rect.collidepoint(event.pos):
            game = 1
            break
        if button_rect1.collidepoint(event.pos):
            game = 2
            break
 for i in range(100):
    animated(name)
 if game == 1:
  while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    clock.tick(50)
    if check() == 2:
        name = "player 1 win"
        break
    elif check() == 0:
        name = "player 2 win"
        break
    elif check() == 1:
        name = "      draw"
        break
    animated(name)
    if current_player == 0:
        name = "players move 1"
    elif current_player >= 1:
        name = "players move 2"
    playermove()
      
 elif game == 2:
    while run:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
     clock.tick(50)
     if check() == 2:
        name = "player win"
        break
     elif check() == 0:
        name = "bot win"
        break
     elif check() == 1:
        name = "      draw"
        break
     if current_player == 0:
        name = "players move"
        animated(name)
        playermove()
     elif current_player >= 1:
        name = "bot move"
        animated(name)
        time.sleep(1)
        #бот
        for i in range(2):
            xo = None
            if i == 0:
               xo = o
            else:
               xo = x
            if cells[0] == xo and cells[2] == xo and point[1] == 0:
                x_o(1)
                break
            elif cells[3] == xo and cells[5] == xo and point[4] == 0:
                x_o(4)
                break 
            elif cells[6] == xo and cells[8] == xo and point[7] == 0:
                x_o(7)
                break
            elif cells[0] == xo and cells[6] == xo and point[3] == 0:
                x_o(3)
                break
            elif cells[1] == xo and cells[7] == xo and point[4] == 0:
                x_o(4)
                break
            elif cells[2] == xo and cells[8] == xo and point[5] == 0:
                x_o(5)
                break
            elif cells[0] == xo and cells[8] == xo and point[4] == 0:
                x_o(4)
                break
            elif cells[2] == xo and cells[6] == xo and point[4] == 0:
                x_o(4)
                break
            elif cells[0] == xo and cells[1] == xo and point[2] == 0:
                x_o(2)
                break
            elif cells[2] == xo and cells[1] == xo and point[0] == 0:
                x_o(0)
                break
            elif cells[3] == xo and cells[4] == xo and point[5] == 0:
                x_o(5)
                break
            elif cells[5] == xo and cells[4] == xo and point[3] == 0:
                x_o(3)
                break
            elif cells[6] == xo and cells[7] == xo and point[8] == 0:
                x_o(8)
                break
            elif cells[8] == xo and cells[7] == xo and point[6] == 0:
                x_o(6)
                break
            elif cells[0] == xo and cells[3] == xo and point[6] == 0:
                x_o(6)
                break
            elif cells[6] == xo and cells[3] == xo and point[0] == 0:
                x_o(0)
                break
            elif cells[1] == xo and cells[4] == xo and point[7] == 0:
                x_o(7)
                break
            elif cells[7] == xo and cells[4] == xo and point[1] == 0:
                x_o(1)
                break
            elif cells[2] == xo and cells[5] == xo and point[8] == 0:
                x_o(8)
                break
            elif cells[8] == xo and cells[5] == xo and point[2] == 0:
                x_o(2)
                break
            elif cells[0] == xo and cells[4] == xo and point[8] == 0:
                x_o(8)
                break
            elif cells[8] == xo and cells[4] == xo and point[0] == 0:
                x_o(0)
                break
            elif cells[2] == xo and cells[4] == xo and point[6] == 0:
                x_o(6)
                break
            elif cells[6] == xo and cells[4] == xo and point[2] == 0:
                x_o(2)
                break
        else:
                esle()
                
     animated(name)
 for i in range(1000):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    win.blit(bg, (0, 0))
    text = FAnt.render(name, True, (255, 255, 255))
    win.blit(text,(175,300))
    pygame.display.update()
pygame.quit()
sys.exit