import sys
import pygame
from pygame import mixer

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

# Screen / Window Size
screen = pygame.display.set_mode((1280, 720))
# Program Title
pygame.display.set_caption("Rewrite")
# Display Refresh
pygame.display.flip()
# Program Icon
icon = pygame.image.load('chibi.jpg')
pygame.display.set_icon(icon)

# Start Menu
def start_menu():
    # Background Music
    mixer.music.load('BGM/CANOE.mp3')
    mixer.music.play(-1)

    # Start, How To Play, Exit Coordinates
    start = pygame.Rect(262, 634, 140, 50)
    instruct = pygame.Rect(492, 634, 343, 50)
    exit = pygame.Rect(930, 634, 120, 50)
    while True:
        # Background Image
        mainscreen = pygame.image.load('BG/Start.jpg')
        screen.blit(mainscreen, (0, 0))
        # Start, How To Play, Exit Images
        startgame = pygame.image.load('START.png')
        screen.blit(startgame, (228, 606))

        howtogame = pygame.image.load('How to Play.png')
        screen.blit(howtogame, (460, 606))

        exitgame = pygame.image.load('EXIT.png')
        screen.blit(exitgame, (900, 606))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start.collidepoint(event.pos):
                    screen1()
                if instruct.collidepoint(event.pos):
                    howtoplay()
                if exit.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        clock.tick(15)

def howtoplay():
    # Instructions BGM
    mixer.music.load('BGM/SOFTWINDFLOWER.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(0.5)

    # Start and Exit Coordinates
    start = pygame.Rect(934, 634, 140, 50)
    exit = pygame.Rect(1130, 634, 120, 50)
    while True:
        # Background Image
        how = pygame.image.load('BG/How To Play.jpg')
        screen.blit(how, (0, 0))

        # Start and Exit Images
        startgame = pygame.image.load('START.png')
        screen.blit(startgame, (900, 606))

        exitgame = pygame.image.load('EXIT.png')
        screen.blit(exitgame, (1100, 606))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start.collidepoint(event.pos):
                    screen1()
                if exit.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        clock.tick(60)

def screen1():
    # Scene 1 BGM
    mixer.music.load('BGM/DAISY.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(0.5)

    # Clickable Whole Screen
    scene1 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page1 = pygame.image.load('BG/1.jpg')
        screen.blit(page1, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene1.collidepoint(event.pos):
                    screen2()
        pygame.display.update()
        clock.tick(60)


def screen2():
    # Clickable Whole Screen
    scene2 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page2 = pygame.image.load('BG/2.jpg')
        screen.blit(page2, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene2.collidepoint(event.pos):
                    screen3()
        pygame.display.update()
        clock.tick(60)


def screen3():
    # Clickable Whole Screen
    scene3 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page3 = pygame.image.load('BG/3.jpg')
        screen.blit(page3, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene3.collidepoint(event.pos):
                    screen4()
        pygame.display.update()
        clock.tick(60)


def screen4():
    # Clickable Whole Screen
    scene4 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page4 = pygame.image.load('BG/4.jpg')
        screen.blit(page4, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene4.collidepoint(event.pos):
                    screen5()
        pygame.display.update()
        clock.tick(60)


def screen5():
    # Clickable Whole Screen
    scene5 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page5 = pygame.image.load('BG/5.jpg')
        screen.blit(page5, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene5.collidepoint(event.pos):
                    screen6()
        pygame.display.update()
        clock.tick(60)


def screen6():
    # Clickable Whole Screen
    scene6 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page6 = pygame.image.load('BG/6.jpg')
        screen.blit(page6, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene6.collidepoint(event.pos):
                    screen7()
        pygame.display.update()
        clock.tick(60)


def screen7():
    # Clickable Whole Screen
    scene7 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page7 = pygame.image.load('BG/7.jpg')
        screen.blit(page7, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene7.collidepoint(event.pos):
                    screen8()
        pygame.display.update()
        clock.tick(60)


def screen8():
    # Clickable Whole Screen
    scene8 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page8 = pygame.image.load('BG/8.jpg')
        screen.blit(page8, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene8.collidepoint(event.pos):
                    screen9()
        pygame.display.update()
        clock.tick(60)


def screen9():
    # Clickable Whole Screen
    scene9 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page9 = pygame.image.load('BG/9.jpg')
        screen.blit(page9, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene9.collidepoint(event.pos):
                    screen10()
        pygame.display.update()
        clock.tick(60)


def screen10():
    # Clickable Whole Screen
    scene10 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page10 = pygame.image.load('BG/10.jpg')
        screen.blit(page10, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene10.collidepoint(event.pos):
                    screen11()
        pygame.display.update()
        clock.tick(60)


def screen11():
    # Clickable Whole Screen
    scene11 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page11 = pygame.image.load('BG/11.jpg')
        screen.blit(page11, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene11.collidepoint(event.pos):
                    screen12()
        pygame.display.update()
        clock.tick(60)


def screen12():
    # Clickable Whole Screen
    scene12 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page12 = pygame.image.load('BG/12.jpg')
        screen.blit(page12, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene12.collidepoint(event.pos):
                    screen13()
        pygame.display.update()
        clock.tick(60)


def screen13():
    # Clickable Whole Screen
    scene13 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page13 = pygame.image.load('BG/13.jpg')
        screen.blit(page13, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene13.collidepoint(event.pos):
                    screen14()
        pygame.display.update()
        clock.tick(60)


def screen14():
    # Clickable Whole Screen
    scene14 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page14 = pygame.image.load('BG/14.jpg')
        screen.blit(page14, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene14.collidepoint(event.pos):
                    screen15()
        pygame.display.update()
        clock.tick(60)


def screen15():
    # Clickable Whole Screen
    scene15 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page15 = pygame.image.load('BG/15.jpg')
        screen.blit(page15, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene15.collidepoint(event.pos):
                    screen16()
        pygame.display.update()
        clock.tick(60)


def screen16():
    # Clickable Whole Screen
    scene16 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page16 = pygame.image.load('BG/16.jpg')
        screen.blit(page16, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene16.collidepoint(event.pos):
                    screen17()
        pygame.display.update()
        clock.tick(60)


def screen17():
    # Clickable Whole Screen
    scene17 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page17 = pygame.image.load('BG/17.jpg')
        screen.blit(page17, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene17.collidepoint(event.pos):
                    screen18()
        pygame.display.update()
        clock.tick(60)


def screen18():
    # Clickable Whole Screen
    scene18 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page18 = pygame.image.load('BG/18.jpg')
        screen.blit(page18, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene18.collidepoint(event.pos):
                    screen19()
        pygame.display.update()
        clock.tick(60)


def screen19():
    # Clickable Whole Screen
    scene19 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page19 = pygame.image.load('BG/19.jpg')
        screen.blit(page19, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene19.collidepoint(event.pos):
                    screen20()
        pygame.display.update()
        clock.tick(60)


def screen20():
    # Clickable Whole Screen
    scene20 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page20 = pygame.image.load('BG/20.jpg')
        screen.blit(page20, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene20.collidepoint(event.pos):
                    screen21()
        pygame.display.update()
        clock.tick(60)


def screen21():
    # Clickable Whole Screen
    scene21 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page21 = pygame.image.load('BG/21.jpg')
        screen.blit(page21, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene21.collidepoint(event.pos):
                    screen22()
        pygame.display.update()
        clock.tick(60)


def screen22():
    # Clickable Whole Screen
    scene22 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page22 = pygame.image.load('BG/22.jpg')
        screen.blit(page22, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene22.collidepoint(event.pos):
                    screen23()
        pygame.display.update()
        clock.tick(60)


def screen23():
    # Clickable Whole Screen
    scene23 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page23 = pygame.image.load('BG/23.jpg')
        screen.blit(page23, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene23.collidepoint(event.pos):
                    screen24()
        pygame.display.update()
        clock.tick(60)


def screen24():
    # Clickable Whole Screen
    scene24 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page24 = pygame.image.load('BG/24.jpg')
        screen.blit(page24, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene24.collidepoint(event.pos):
                    screen25()
        pygame.display.update()
        clock.tick(60)


def screen25():
    # Clickable Whole Screen
    scene25 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page25 = pygame.image.load('BG/25.jpg')
        screen.blit(page25, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene25.collidepoint(event.pos):
                    screen26()
        pygame.display.update()
        clock.tick(60)


def screen26():
    # Clickable Whole Screen
    scene26 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page26 = pygame.image.load('BG/26.jpg')
        screen.blit(page26, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene26.collidepoint(event.pos):
                    choice()
        pygame.display.update()
        clock.tick(60)


def choice():
    # Clickable Whole Screen
    hallway1 = pygame.Rect(64, 103, 457, 457)
    cafeteria1 = pygame.Rect(734, 100, 457, 467)
    while True:
        # Background Image
        page27 = pygame.image.load('BG/27.jpg')
        screen.blit(page27, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway1.collidepoint(event.pos):
                    hallway_1()
                if cafeteria1.collidepoint(event.pos):
                    cafeteria_1()
        pygame.display.update()
        clock.tick(60)


def hallway_1():
    # Hallway BGM
    mixer.music.load('BGM/FRUIT.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(0.5)
    # Clickable Whole Screen
    hallway1 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage1 = pygame.image.load('BG/hallway1.jpg')
        screen.blit(hallwaypage1, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway1.collidepoint(event.pos):
                    hallway_2()
        pygame.display.update()
        clock.tick(60)


def hallway_2():
    # Clickable Whole Screen
    hallway2 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage2 = pygame.image.load('BG/hallway2.jpg')
        screen.blit(hallwaypage2, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway2.collidepoint(event.pos):
                    hallway_3()
        pygame.display.update()
        clock.tick(60)


def hallway_3():
    # Clickable Whole Screen
    hallway3 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage3 = pygame.image.load('BG/hallway3.jpg')
        screen.blit(hallwaypage3, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway3.collidepoint(event.pos):
                    hallway_4()
        pygame.display.update()
        clock.tick(60)


def hallway_4():
    # Clickable Whole Screen
    hallway4 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage4 = pygame.image.load('BG/hallway4.jpg')
        screen.blit(hallwaypage4, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway4.collidepoint(event.pos):
                    hallway_5()
        pygame.display.update()
        clock.tick(60)


def hallway_5():
    # Clickable Whole Screen
    hallway5 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage5 = pygame.image.load('BG/hallway5.jpg')
        screen.blit(hallwaypage5, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway5.collidepoint(event.pos):
                    hallway_6()
        pygame.display.update()
        clock.tick(60)


def hallway_6():
    # Clickable Whole Screen
    hallway6 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage6 = pygame.image.load('BG/hallway6.jpg')
        screen.blit(hallwaypage6, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway6.collidepoint(event.pos):
                    hallway_7()
        pygame.display.update()
        clock.tick(60)


def hallway_7():
    # Clickable Whole Screen
    hallway7 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage7 = pygame.image.load('BG/hallway7.jpg')
        screen.blit(hallwaypage7, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway7.collidepoint(event.pos):
                    hallway_8()
        pygame.display.update()
        clock.tick(60)


def hallway_8():
    # Clickable Whole Screen
    hallway8 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage8 = pygame.image.load('BG/hallway8.jpg')
        screen.blit(hallwaypage8, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway8.collidepoint(event.pos):
                    hallway_9()
        pygame.display.update()
        clock.tick(60)


def hallway_9():
    # Clickable Whole Screen
    hallway9 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage9 = pygame.image.load('BG/hallway9.jpg')
        screen.blit(hallwaypage9, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway9.collidepoint(event.pos):
                    hallway_10()
        pygame.display.update()
        clock.tick(60)


def hallway_10():
    # Clickable Whole Screen
    hallway10 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage10 = pygame.image.load('BG/hallway10.jpg')
        screen.blit(hallwaypage10, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway10.collidepoint(event.pos):
                    hallway_11()
        pygame.display.update()
        clock.tick(60)


def hallway_11():
    # Clickable Whole Screen
    hallway11 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage11 = pygame.image.load('BG/hallway11.jpg')
        screen.blit(hallwaypage11, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway11.collidepoint(event.pos):
                    hallway_12()
        pygame.display.update()
        clock.tick(60)


def hallway_12():
    # Clickable Whole Screen
    hallway12 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage12 = pygame.image.load('BG/hallway12.jpg')
        screen.blit(hallwaypage12, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway12.collidepoint(event.pos):
                    hallway_13()
        pygame.display.update()
        clock.tick(60)


def hallway_13():
    # Clickable Whole Screen
    hallway13 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage13 = pygame.image.load('BG/hallway13.jpg')
        screen.blit(hallwaypage13, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway13.collidepoint(event.pos):
                    hallway_14()
        pygame.display.update()
        clock.tick(60)


def hallway_14():
    # Clickable Whole Screen
    hallway14 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage14 = pygame.image.load('BG/hallway14.jpg')
        screen.blit(hallwaypage14, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway14.collidepoint(event.pos):
                    hallway_15()
        pygame.display.update()
        clock.tick(60)


def hallway_15():
    # Clickable Whole Screen
    hallway15 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage15 = pygame.image.load('BG/hallway15.jpg')
        screen.blit(hallwaypage15, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway15.collidepoint(event.pos):
                    hallway_16()
        pygame.display.update()
        clock.tick(60)


def hallway_16():
    # Clickable Whole Screen
    hallway16 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage16 = pygame.image.load('BG/hallway16.jpg')
        screen.blit(hallwaypage16, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway16.collidepoint(event.pos):
                    hallway_17()
        pygame.display.update()
        clock.tick(60)


def hallway_17():
    # Clickable Whole Screen
    hallway17 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage17 = pygame.image.load('BG/hallway17.jpg')
        screen.blit(hallwaypage17, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway17.collidepoint(event.pos):
                    hallway_18()
        pygame.display.update()
        clock.tick(60)


def hallway_18():
    # Clickable Whole Screen
    hallway18 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage18 = pygame.image.load('BG/hallway18.jpg')
        screen.blit(hallwaypage18, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway18.collidepoint(event.pos):
                    hallway_19()
        pygame.display.update()
        clock.tick(60)


def hallway_19():
    # Clickable Whole Screen
    hallway19 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage19 = pygame.image.load('BG/hallway19.jpg')
        screen.blit(hallwaypage19, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway19.collidepoint(event.pos):
                    Shizuru_End()
        pygame.display.update()
        clock.tick(60)


def Shizuru_End():
    # Clickable Whole Screen
    Shizuru = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        ShizuruEnd = pygame.image.load('BG/Shizuru End.jpg')
        screen.blit(ShizuruEnd, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Shizuru.collidepoint(event.pos):
                    screen26L()
        pygame.display.update()
        clock.tick(60)


def cafeteria_1():
    # Cafeteria BGM
    mixer.music.load('BGM/ANTHRURIUM.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(0.5)
    # Clickable Whole Screen
    cafe1 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        cafepage1 = pygame.image.load('BG/cafe1.jpg')
        screen.blit(cafepage1, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cafe1.collidepoint(event.pos):
                    cafeteria_2()
        pygame.display.update()
        clock.tick(60)

def cafeteria_2():
    # Clickable Whole Screen
    cafe2 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        cafepage2 = pygame.image.load('BG/cafe2.jpg')
        screen.blit(cafepage2, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cafe2.collidepoint(event.pos):
                    cafeteria_3()
        pygame.display.update()
        clock.tick(60)

def cafeteria_3():
    # Clickable Whole Screen
    cafe3 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        cafepage3 = pygame.image.load('BG/cafe3.jpg')
        screen.blit(cafepage3, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cafe3.collidepoint(event.pos):
                    cafeteria_4()
        pygame.display.update()
        clock.tick(60)

def cafeteria_4():
    # Clickable Whole Screen
    cafe4 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        cafepage4 = pygame.image.load('BG/cafe4.jpg')
        screen.blit(cafepage4, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cafe4.collidepoint(event.pos):
                    cafeteria_5()
        pygame.display.update()
        clock.tick(60)

def cafeteria_5():
    # Clickable Whole Screen
    cafe5 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        cafepage5 = pygame.image.load('BG/cafe5.jpg')
        screen.blit(cafepage5, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cafe5.collidepoint(event.pos):
                    cafeteria_6()
        pygame.display.update()
        clock.tick(60)

def cafeteria_6():
    # Clickable Whole Screen
    cafe6 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        cafepage6 = pygame.image.load('BG/cafe6.jpg')
        screen.blit(cafepage6, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cafe6.collidepoint(event.pos):
                    cafeteria_7()
        pygame.display.update()
        clock.tick(60)

def cafeteria_7():
    # Clickable Whole Screen
    cafe7 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        cafepage7 = pygame.image.load('BG/cafe7.jpg')
        screen.blit(cafepage7, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cafe7.collidepoint(event.pos):
                    cafeteria_8()
        pygame.display.update()
        clock.tick(60)

def cafeteria_8():
    # Clickable Whole Screen
    cafe8 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        cafepage8 = pygame.image.load('BG/cafe8.jpg')
        screen.blit(cafepage8, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cafe8.collidepoint(event.pos):
                    cafeteria_9()
        pygame.display.update()
        clock.tick(60)

def cafeteria_9():
    # Clickable Whole Screen
    cafe9 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        cafepage9 = pygame.image.load('BG/cafe9.jpg')
        screen.blit(cafepage9, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cafe9.collidepoint(event.pos):
                    cafeteria_10()
        pygame.display.update()
        clock.tick(60)

def cafeteria_10():
    # Clickable Whole Screen
    cafe10 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        cafepage10 = pygame.image.load('BG/cafe10.jpg')
        screen.blit(cafepage10, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cafe10.collidepoint(event.pos):
                    cafeteria_11()
        pygame.display.update()
        clock.tick(60)

def cafeteria_11():
    # Clickable Whole Screen
    cafe11 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        cafepage11 = pygame.image.load('BG/cafe11.jpg')
        screen.blit(cafepage11, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cafe11.collidepoint(event.pos):
                    cafeteria_12()
        pygame.display.update()
        clock.tick(60)

def cafeteria_12():
    # Clickable Whole Screen
    cafe12 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        cafepage12 = pygame.image.load('BG/cafe12.jpg')
        screen.blit(cafepage12, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cafe12.collidepoint(event.pos):
                    Lucia_End()
        pygame.display.update()
        clock.tick(60)

def Lucia_End():
    # Clickable Whole Screen
    Lucia = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        LuciaEnd = pygame.image.load('BG/Lucia End.png')
        screen.blit(LuciaEnd, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Lucia.collidepoint(event.pos):
                    screen26S()
        pygame.display.update()
        clock.tick(60)

def screen26L():
    mixer.music.load('BGM/DAISY.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(0.5)
    # Clickable Whole Screen
    scene26 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page26 = pygame.image.load('BG/26.jpg')
        screen.blit(page26, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene26.collidepoint(event.pos):
                    choiceL()
        pygame.display.update()
        clock.tick(60)


def choiceL():
    # Clickable Whole Screen
    cafeteria1 = pygame.Rect(428, 103, 457, 457)
    while True:
        # Background Image
        page27 = pygame.image.load('BG/choicelucia.jpg')
        screen.blit(page27, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cafeteria1.collidepoint(event.pos):
                    cafeteria_1L()
        pygame.display.update()
        clock.tick(60)

def cafeteria_1L():
    # Cafeteria BGM
    mixer.music.load('BGM/ANTHRURIUM.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(0.5)
    # Clickable Whole Screen
    cafe1 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        cafepage1 = pygame.image.load('BG/cafe1.jpg')
        screen.blit(cafepage1, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cafe1.collidepoint(event.pos):
                    cafeteria_2L()
        pygame.display.update()
        clock.tick(60)

def cafeteria_2L():
    # Clickable Whole Screen
    cafe2 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        cafepage2 = pygame.image.load('BG/cafe2.jpg')
        screen.blit(cafepage2, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cafe2.collidepoint(event.pos):
                    cafeteria_3L()
        pygame.display.update()
        clock.tick(60)

def cafeteria_3L():
    # Clickable Whole Screen
    cafe3 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        cafepage3 = pygame.image.load('BG/cafe3.jpg')
        screen.blit(cafepage3, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cafe3.collidepoint(event.pos):
                    cafeteria_4L()
        pygame.display.update()
        clock.tick(60)

def cafeteria_4L():
    # Clickable Whole Screen
    cafe4 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        cafepage4 = pygame.image.load('BG/cafe4.jpg')
        screen.blit(cafepage4, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cafe4.collidepoint(event.pos):
                    cafeteria_5L()
        pygame.display.update()
        clock.tick(60)

def cafeteria_5L():
    # Clickable Whole Screen
    cafe5 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        cafepage5 = pygame.image.load('BG/cafe5.jpg')
        screen.blit(cafepage5, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cafe5.collidepoint(event.pos):
                    cafeteria_6L()
        pygame.display.update()
        clock.tick(60)

def cafeteria_6L():
    # Clickable Whole Screen
    cafe6 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        cafepage6 = pygame.image.load('BG/cafe6.jpg')
        screen.blit(cafepage6, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cafe6.collidepoint(event.pos):
                    cafeteria_7L()
        pygame.display.update()
        clock.tick(60)

def cafeteria_7L():
    # Clickable Whole Screen
    cafe7 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        cafepage7 = pygame.image.load('BG/cafe7.jpg')
        screen.blit(cafepage7, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cafe7.collidepoint(event.pos):
                    cafeteria_8L()
        pygame.display.update()
        clock.tick(60)

def cafeteria_8L():
    # Clickable Whole Screen
    cafe8 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        cafepage8 = pygame.image.load('BG/cafe8.jpg')
        screen.blit(cafepage8, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cafe8.collidepoint(event.pos):
                    cafeteria_9L()
        pygame.display.update()
        clock.tick(60)

def cafeteria_9L():
    # Clickable Whole Screen
    cafe9 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        cafepage9 = pygame.image.load('BG/cafe9.jpg')
        screen.blit(cafepage9, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cafe9.collidepoint(event.pos):
                    cafeteria_10L()
        pygame.display.update()
        clock.tick(60)

def cafeteria_10L():
    # Clickable Whole Screen
    cafe10 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        cafepage10 = pygame.image.load('BG/cafe10.jpg')
        screen.blit(cafepage10, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cafe10.collidepoint(event.pos):
                    cafeteria_11L()
        pygame.display.update()
        clock.tick(60)

def cafeteria_11L():
    # Clickable Whole Screen
    cafe11 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        cafepage11 = pygame.image.load('BG/cafe11.jpg')
        screen.blit(cafepage11, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cafe11.collidepoint(event.pos):
                    cafeteria_12L()
        pygame.display.update()
        clock.tick(60)

def cafeteria_12L():
    # Clickable Whole Screen
    cafe12 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        cafepage12 = pygame.image.load('BG/cafe12.jpg')
        screen.blit(cafepage12, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cafe12.collidepoint(event.pos):
                    Lucia_EndL()
        pygame.display.update()
        clock.tick(60)

def Lucia_EndL():
    # Clickable Whole Screen
    Lucia = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        LuciaEnd = pygame.image.load('BG/Lucia End.png')
        screen.blit(LuciaEnd, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Lucia.collidepoint(event.pos):
                    start_menu()
        pygame.display.update()
        clock.tick(60)

def screen26S():
    mixer.music.load('BGM/DAISY.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(0.5)
    # Clickable Whole Screen
    scene26 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        page26 = pygame.image.load('BG/26.jpg')
        screen.blit(page26, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene26.collidepoint(event.pos):
                    choiceS()
        pygame.display.update()
        clock.tick(60)


def choiceS():
    # Clickable Whole Screen
    hallway1 = pygame.Rect(430, 102, 457, 457)
    while True:
        # Background Image
        page27 = pygame.image.load('BG/choiceshizuru.jpg')
        screen.blit(page27, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway1.collidepoint(event.pos):
                    hallway_1S()
        pygame.display.update()
        clock.tick(60)

def hallway_1S():
    # Hallway BGM
    mixer.music.load('BGM/FRUIT.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(0.5)
    # Clickable Whole Screen
    hallway1 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage1 = pygame.image.load('BG/hallway1.jpg')
        screen.blit(hallwaypage1, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway1.collidepoint(event.pos):
                    hallway_2S()
        pygame.display.update()
        clock.tick(60)


def hallway_2S():
    # Clickable Whole Screen
    hallway2 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage2 = pygame.image.load('BG/hallway2.jpg')
        screen.blit(hallwaypage2, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway2.collidepoint(event.pos):
                    hallway_3S()
        pygame.display.update()
        clock.tick(60)


def hallway_3S():
    # Clickable Whole Screen
    hallway3 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage3 = pygame.image.load('BG/hallway3.jpg')
        screen.blit(hallwaypage3, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway3.collidepoint(event.pos):
                    hallway_4S()
        pygame.display.update()
        clock.tick(60)


def hallway_4S():
    # Clickable Whole Screen
    hallway4 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage4 = pygame.image.load('BG/hallway4.jpg')
        screen.blit(hallwaypage4, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway4.collidepoint(event.pos):
                    hallway_5S()
        pygame.display.update()
        clock.tick(60)


def hallway_5S():
    # Clickable Whole Screen
    hallway5 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage5 = pygame.image.load('BG/hallway5.jpg')
        screen.blit(hallwaypage5, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway5.collidepoint(event.pos):
                    hallway_6S()
        pygame.display.update()
        clock.tick(60)


def hallway_6S():
    # Clickable Whole Screen
    hallway6 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage6 = pygame.image.load('BG/hallway6.jpg')
        screen.blit(hallwaypage6, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway6.collidepoint(event.pos):
                    hallway_7S()
        pygame.display.update()
        clock.tick(60)


def hallway_7S():
    # Clickable Whole Screen
    hallway7 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage7 = pygame.image.load('BG/hallway7.jpg')
        screen.blit(hallwaypage7, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway7.collidepoint(event.pos):
                    hallway_8S()
        pygame.display.update()
        clock.tick(60)


def hallway_8S():
    # Clickable Whole Screen
    hallway8 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage8 = pygame.image.load('BG/hallway8.jpg')
        screen.blit(hallwaypage8, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway8.collidepoint(event.pos):
                    hallway_9S()
        pygame.display.update()
        clock.tick(60)


def hallway_9S():
    # Clickable Whole Screen
    hallway9 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage9 = pygame.image.load('BG/hallway9.jpg')
        screen.blit(hallwaypage9, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway9.collidepoint(event.pos):
                    hallway_10S()
        pygame.display.update()
        clock.tick(60)


def hallway_10S():
    # Clickable Whole Screen
    hallway10 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage10 = pygame.image.load('BG/hallway10.jpg')
        screen.blit(hallwaypage10, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway10.collidepoint(event.pos):
                    hallway_11S()
        pygame.display.update()
        clock.tick(60)


def hallway_11S():
    # Clickable Whole Screen
    hallway11 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage11 = pygame.image.load('BG/hallway11.jpg')
        screen.blit(hallwaypage11, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway11.collidepoint(event.pos):
                    hallway_12S()
        pygame.display.update()
        clock.tick(60)


def hallway_12S():
    # Clickable Whole Screen
    hallway12 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage12 = pygame.image.load('BG/hallway12.jpg')
        screen.blit(hallwaypage12, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway12.collidepoint(event.pos):
                    hallway_13S()
        pygame.display.update()
        clock.tick(60)


def hallway_13S():
    # Clickable Whole Screen
    hallway13 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage13 = pygame.image.load('BG/hallway13.jpg')
        screen.blit(hallwaypage13, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway13.collidepoint(event.pos):
                    hallway_14S()
        pygame.display.update()
        clock.tick(60)


def hallway_14S():
    # Clickable Whole Screen
    hallway14 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage14 = pygame.image.load('BG/hallway14.jpg')
        screen.blit(hallwaypage14, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway14.collidepoint(event.pos):
                    hallway_15S()
        pygame.display.update()
        clock.tick(60)


def hallway_15S():
    # Clickable Whole Screen
    hallway15 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage15 = pygame.image.load('BG/hallway15.jpg')
        screen.blit(hallwaypage15, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway15.collidepoint(event.pos):
                    hallway_16S()
        pygame.display.update()
        clock.tick(60)


def hallway_16S():
    # Clickable Whole Screen
    hallway16 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage16 = pygame.image.load('BG/hallway16.jpg')
        screen.blit(hallwaypage16, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway16.collidepoint(event.pos):
                    hallway_17S()
        pygame.display.update()
        clock.tick(60)


def hallway_17S():
    # Clickable Whole Screen
    hallway17 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage17 = pygame.image.load('BG/hallway17.jpg')
        screen.blit(hallwaypage17, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway17.collidepoint(event.pos):
                    hallway_18S()
        pygame.display.update()
        clock.tick(60)


def hallway_18S():
    # Clickable Whole Screen
    hallway18 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage18 = pygame.image.load('BG/hallway18.jpg')
        screen.blit(hallwaypage18, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway18.collidepoint(event.pos):
                    hallway_19S()
        pygame.display.update()
        clock.tick(60)


def hallway_19S():
    # Clickable Whole Screen
    hallway19 = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        hallwaypage19 = pygame.image.load('BG/hallway19.jpg')
        screen.blit(hallwaypage19, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hallway19.collidepoint(event.pos):
                    Shizuru_EndS()
        pygame.display.update()
        clock.tick(60)


def Shizuru_EndS():
    # Clickable Whole Screen
    Shizuru = pygame.Rect(0, 0, 1280, 720)

    while True:
        # Background Image
        ShizuruEnd = pygame.image.load('BG/Shizuru End.jpg')
        screen.blit(ShizuruEnd, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Click Command Next Page
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Shizuru.collidepoint(event.pos):
                    start_menu()
        pygame.display.update()
        clock.tick(60)

# Game Loop
running = True
while running:
    start_menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(60)
