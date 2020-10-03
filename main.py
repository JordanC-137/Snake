import pygame
import random
pygame.init

win = pygame.display.set_mode((500, 700))
pygame.display.set_caption("Game")
listOfValues = []
direction = "RIGHT"

def directionChange():
    direction = getDirection()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and direction != "RIGHT":
        setDirection("LEFT")
    if keys[pygame.K_RIGHT] and direction != "LEFT":
        setDirection("RIGHT")
    if keys[pygame.K_UP] and direction != "DOWN":
        setDirection("UP")
    if keys[pygame.K_DOWN] and direction != "UP":
        setDirection("DOWN")

def setDirection(newDir):
    global direction
    if newDir == "RIGHT" or newDir == "LEFT" or newDir == "UP" or newDir == "DOWN":
        direction = newDir

def getDirection():
    global direction
    return direction

def getWindow():
    global win
    return win

def drawBoundaries():
    win = getWindow()
    #pygame.draw.rect(surface, (colour), (x, y, width, height))
    pygame.draw.rect(win, (0, 0, 255), (0, 0, 10, (700 - 10)))
    pygame.draw.rect(win, (0, 0, 255), (490, 0, 10, (700 - 10)))
    pygame.draw.rect(win, (0, 0, 255), (0, 0, 500, 10))
    pygame.draw.rect(win, (0, 0, 255), (0, 490, 500, 10))
    pygame.draw.rect(win, (0, 0, 255), (0, 690, 500, 10))

#Generate tuple of 2 random numbers
def randomFood():
    return (random.randint(1, 48) * 10, random.randint(1, 48) * 10)

def drawString(text, window, location):
    pygame.font.init()
    myFont = pygame.font.SysFont('Ariel Black', 70)
    textsurface = myFont.render(text, False, (255, 255, 255))
    window.blit(textsurface, location)


def gameLoop():
    running = True
    win = getWindow()
    playerX, playerY, speed = 50, 50, 10
    food = randomFood()
    gameOver = False
    while running:
        if not gameOver:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            directionChange()
            if getDirection() == "LEFT":
                playerX -= speed
            elif getDirection() == "RIGHT":
                playerX += speed
            elif getDirection() == "DOWN":
                playerY += speed
            elif getDirection() == "UP":
                playerY -= speed
            win.fill((0, 0, 0))
            drawBoundaries()
            if playerX == 0 or playerX == 490 or playerY == 0 or playerY == 490 or (playerX, playerY) in listOfValues:
                gameOver = True
                pass
            listOfValues.insert(0, (playerX, playerY))
            if food == listOfValues[0]:
                for i in range(3):
                    listOfValues.append((playerX, playerY))
            if food in listOfValues:
                food = randomFood()
            for i in listOfValues:
                pygame.draw.rect(win, (255, 255, 255), ((i[0], i[1], 10, 10)))
            listOfValues.pop()
            drawString("Score: " + str(len(listOfValues) + 1), getWindow(), (250 - 80, 500 + (100)))
            pygame.draw.rect(win, (0, 255, 0), (food[0], food[1], 10, 10))
            pygame.display.update()
        else:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            win.fill((0, 0, 0))
            drawString("Score: " + str(len(listOfValues) + 1), getWindow(), (150, 250))
            pygame.display.update()

gameLoop()