from distutils.command.build import build
from random import randrange
import pygame
from sys import exit
import time

#Classe qui paramètre le tableau des scores
class Score:
    textX = 10
    textY = 10
    score_value = 0

#Classe qui paramètre de les dimensions de la fenetre 
class Screen:
    screenX = 800
    screenY = 800

#Classe qui paramètre la position de vie dans la fenetre 
class Live:
    LiveX = 10
    LiveY = 50

#Classe qui paramètre la position du joueur
class SetUpPlayer:
    SetupplayerX = 174
    SetupplayerY = 600

#Classe qui paramètre la rapidité du jeu vel pour le joueur et gravity pour la balle
class SetUpQuickGame:
    gravity = 3
    vel = 10
    numberLive = 3

#Fonction d'affichage du score
def showScore(scoreInit, screen, font):
    score = font.render("Score : " + str(scoreInit.score_value), True, (0, 0, 0))
    screen.blit(score, (scoreInit.textX, scoreInit.textY))

def ShowLive(numberLive, screen, font): 
    lives = font.render("X " + str(numberLive), True, (0, 0, 0))
    screen.blit(lives, (60, 55))

#Fonction d'affichage d'ecran du game over
def gameOverScreen(screen, font):
            gameOver = font.render(" Game over ", True, (255, 255, 255))
            screen.fill((0,0,0))
            screen.blit(gameOver,(300, 400))
            pygame.display.update()
            time.sleep(5)
            pygame.quit()
            exit()

#Fonction qui permet de faire bouger le joueur
def keyEvent(x, border, vel):
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT] :
        if (x > 0) :
            x -= vel
    if userInput[pygame.K_RIGHT] :
        if (x < (border - 174)):
            x += vel
    return (x)

#Fonction qui gère le respawn du joueur et ennemi
def respawn(ScreenInit, tapiocaRect):
    tapiocaRect.x = randrange(ScreenInit.screenX - 121)
    tapiocaRect.y = 0

#Fonction qui gère la collision du joueur et ennemi
def collision(tapiocaRect, ScreenInit, scoreInit, SetUpQuickGameInit):
    scoreInit.score_value += 1
    SetUpQuickGameInit.gravity += 1
    respawn(ScreenInit, tapiocaRect)

#Fonction qui gère le fait de perdre une vie
def hit(SetUpQuickGameInit, ScreenInit,tapiocaRect):
    SetUpQuickGameInit.numberLive -= 1
    respawn(ScreenInit, tapiocaRect)

#Fonction Main
def main():
    scoreInit = Score()
    ScreenInit = Screen()
    SetUpPlayerInit = SetUpPlayer()
    SetUpQuickGameInit = SetUpQuickGame()
    LiveInit = Live()

    pygame.init()
    screen = pygame.display.set_mode((ScreenInit.screenX, ScreenInit.screenY))
    pygame.display.set_caption('bubble collect')
    font = pygame.font.SysFont('arial', 32)

    bk = pygame.image.load('background_800_800.png').convert_alpha()

    live = pygame.image.load('live.png').convert_alpha()


    player = pygame.image.load('bottlexs.png').convert_alpha()
    playerRect = player.get_rect(topleft = (SetUpPlayerInit.SetupplayerX, SetUpPlayerInit.SetupplayerY))
    tapioca = pygame.image.load('bubzsmall.png').convert_alpha()
    tapiocaRect = tapioca.get_rect(topleft = (randrange(ScreenInit.screenX), 0))

    while True : 
        screen.fill((0,0,0))
        screen.blit(bk, (int(0), int(0)))
        screen.blit(player,(int(playerRect.x), int(playerRect.y)))
        screen.blit(tapioca,(int(tapiocaRect.x), int(tapiocaRect.y)))
        screen.blit(live,(int(LiveInit.LiveX), int(LiveInit.LiveY)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        playerRect.x = keyEvent(playerRect.x, ScreenInit.screenX, SetUpQuickGameInit.vel)
        tapiocaRect.y = tapiocaRect.y + SetUpQuickGameInit.gravity

        pygame.time.delay(35)

        if playerRect.colliderect(tapiocaRect):
            collision(tapiocaRect, ScreenInit, scoreInit, SetUpQuickGameInit)
        
        if (SetUpQuickGameInit.numberLive == 0):
            gameOverScreen(screen, font)
        
        if (tapiocaRect.y > ScreenInit.screenY):
            hit(SetUpQuickGameInit, ScreenInit,tapiocaRect)

        showScore(scoreInit, screen, font)
        ShowLive(SetUpQuickGameInit.numberLive, screen, font)

        pygame.display.update()

if __name__ == '__main__':
    main()