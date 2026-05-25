#################################################################################################
#################################################################################################
##                                                                                             ##
##  ##      #          #            ##        ##    ##    #    ###########       ##########    ##
##  ##     #          # #           ##      # ##    ##   #     ##                ##        #   ##
##  ##   #           #   #          ##     #  ##    ##  #      ##                ##        #   ##
##  ## #            #     #         ##    #   ##    ## #       ##                ##########    ##
##  ###            #       #        ##   #    ##    ###        ###########       ##            ##
##  ## #          #         #       ##  #     ##    ## #       ##                ##            ##
##  ##  #        #           #      ## #      ##    ##  #      ##                ##            ##
##  ##   #      #             #     ###       ##    ##   #     ##                ##            ##
##  ##    #    #               #    ##        ##    ##    #    ###########       ##            ##
##                                                                                             ##
#################################################################################################
#################################################################################################

import pygame
import time

#настройка pygame
pygame.init()
screen = pygame.display.set_mode((1950,1150))
font = pygame.font.Font(None,34)
bigfont = pygame.font.Font(None,100)
pygame.display.set_icon(pygame.image.load("apple.png.ico"))

#настройки к игре
f = open(".venv/money")
rf = open(".venv/rulist")
bf = open(".venv/bogat")
money = int(f.readline())
r = int(rf.readline())
bogat = int(bf.readline())

if r == 0:
    if money < 4000000 and bogat == 0:
        pygame.display.set_caption("пройди игру перед выходом")
        room = pygame.image.load(".venv/Безымянный.png")
    else:
        pygame.display.set_caption("ну ты хоть что то прошёл")
        room = pygame.image.load(".venv/ымянный.png")
else:
    if money < 4000000 and bogat == 0:
        pygame.display.set_caption("познай силу нерослопа")
        room = pygame.image.load("images/r/rБезымянный.png")
    else:
        pygame.display.set_caption("тебе действительно это нравится?")
        room = pygame.image.load("images/r/rымянный.png")
f.close()
rf.close()
bf.close()

f =  open(".venv/money","w")
rf = open(".venv/rulist","w")
bf = open(".venv/bogat","w")
rf.write(str(r))
bf.write(str(bogat))

clicktype = 0
clicktick = 0

if r == 0:
    apple =      pygame.image.load("images/apple.png.png")
    banana =     pygame.image.load("images/banana.png")
    pumkin =     pygame.image.load("images/pumkin.png")
    pineapple =  pygame.image.load("images/pineapple.png")
    plum =       pygame.image.load("images/plum.png")
    gold_apple = pygame.image.load("images/goldapple.png")
else:
    apple =      pygame.image.load("images/r/rapple.png.png")
    banana =     pygame.image.load("images/r/rbanana.png")
    pumkin =     pygame.image.load("images/r/rpumkin.png")
    pineapple =  pygame.image.load("images/r/rpineapple.png")
    plum =       pygame.image.load("images/r/rplum.png")
    gold_apple = pygame.image.load("images/r/rgoldapple.png")



run = True
while run:
    pygame.time.Clock().tick(60)
    click = False

    #ивенты
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
           click = True

    #игра

    screen.fill((0,0,0))

    if clicktick > 0:
        clicktick -= 1
    elif clicktick == 0:
        clicktype = 0

    screen.blit(room, (0, 150))
    if clicktype == 1:
        screen.blit(apple, (350, 600))
    if clicktype == 2:
        screen.blit(banana, (350, 600))
    if clicktype == 3:
        screen.blit(pumkin, (350, 600))
    if clicktype == 4:
        screen.blit(pineapple, (350, 600))
    if clicktype == 5:
        screen.blit(plum, (350, 600))
    if clicktype == 6:
        screen.blit(gold_apple, (350, 600))

    if r == 0:
        if money >= 100:
            pygame.draw.rect(screen, (255,0,0), (775, 500, 100, 35))
        else:
            pygame.draw.rect(screen, (71,0,0), (775, 500, 100, 35))
        if money >= 1000:
            pygame.draw.rect(screen, (224, 169, 2), (775, 550, 100, 35))
        else:
            pygame.draw.rect(screen, (156, 117, 0), (775, 550, 100, 35))
        if money >= 10000:
            pygame.draw.rect(screen, (247, 99, 0), (775, 600, 100, 35))
        else:
            pygame.draw.rect(screen, (51, 32, 0), (775, 600, 100, 35))
        if money >= 100000:
            pygame.draw.rect(screen, (174, 255, 0), (890, 500, 100, 35))
        else:
            pygame.draw.rect(screen, (58, 84, 0), (890, 500, 100, 35))
        if money >= 500000:
            pygame.draw.rect(screen, (73, 2, 227), (890, 550, 100, 35))
        else:
            pygame.draw.rect(screen, (32, 0, 102), (890, 550, 100, 35))
        if money >= 1000000:
            pygame.draw.rect(screen, (251,255,0), (890, 600, 110, 35))
        elif money <= 1000:
            pygame.draw.rect(screen, (0,0,0), (890, 600, 110, 35))
        elif money <= 10000:
            pygame.draw.rect(screen, (68, 69, 0), (890, 600, 110, 35))
        elif money <= 100000:
            pygame.draw.rect(screen, (128, 130, 0), (890, 600, 110, 35))
        elif money <= 1000000 and money >= 100000:
            pygame.draw.rect(screen, (170, 179, 0), (890, 600, 110, 35))

    else:
        if money >= 100:
            pygame.draw.rect(screen, (255, 0, 0), (775, 520, 100, 35))
        else:
            pygame.draw.rect(screen, (71, 0, 0), (775, 520, 100, 35))
        if money >= 1000:
            pygame.draw.rect(screen, (224, 169, 2), (775, 570, 100, 35))
        else:
            pygame.draw.rect(screen, (156, 117, 0), (775, 570, 100, 35))
        if money >= 10000:
            pygame.draw.rect(screen, (247, 99, 0), (775, 620, 100, 35))
        else:
            pygame.draw.rect(screen, (51, 32, 0), (775, 620, 100, 35))
        if money >= 100000:
            pygame.draw.rect(screen, (174, 255, 0), (890, 520, 100, 35))
        else:
            pygame.draw.rect(screen, (58, 84, 0), (890, 520, 100, 35))
        if money >= 500000:
            pygame.draw.rect(screen, (73, 2, 227), (890, 570, 100, 35))
        else:
            pygame.draw.rect(screen, (32, 0, 102), (890, 570, 100, 35))
        if money >= 1000000:
            pygame.draw.rect(screen, (251, 255, 0), (890, 620, 110, 35))
        elif money <= 1000:
            pygame.draw.rect(screen, (0, 0, 0), (890, 620, 110, 35))
        elif money <= 10000:
            pygame.draw.rect(screen, (68, 69, 0), (890, 620, 110, 35))
        elif money <= 100000:
            pygame.draw.rect(screen, (128, 130, 0), (890, 620, 110, 35))
        elif money <= 1000000 and money >= 100000:
            pygame.draw.rect(screen, (170, 179, 0), (890, 620, 110, 35))

    if bogat == 1:
        pygame.draw.rect(screen, (170, 179, 0), (1600, 155, 140, 35))
        screen.blit(font.render("Перезапуск", True, (255,255,255)), (1600, 155))

    if r == 0:
        screen.blit(font.render("100"    , True, (255,255,255)), (795, 510))
        screen.blit(font.render("1 000"  , True, (255,255,255)), (795, 560))
        screen.blit(font.render("10 000" , True, (255,255,255)), (790, 610))
        screen.blit(font.render("100 000", True, (255,255,255)), (900, 510))
        screen.blit(font.render("500 000", True, (255,255,255)), (900, 560))
        screen.blit(font.render("1 000 000", True, (255,255,255)), (889, 610))
    else:
        screen.blit(font.render("100"    , True, (255,255,255)), (795, 530))
        screen.blit(font.render("1 000"  , True, (255,255,255)), (795, 580))
        screen.blit(font.render("10 000" , True, (255,255,255)), (790, 630))
        screen.blit(font.render("100 000", True, (255,255,255)), (900, 530))
        screen.blit(font.render("500 000", True, (255,255,255)), (900, 580))
        screen.blit(font.render("1 000 000", True, (255,255,255)), (889, 630))


    pygame.draw.rect(screen, (255,0,0), (215, 950, 100, 35))
    screen.blit(font.render("Выход", True, (255,255,255)), (215,955))

    if bogat == 0:
        screen.blit(font.render(f"Деньги:{money} / 4 000 000",True,(0,0,0)),(210,155))
        screen.blit(font.render("Накопи на квартиру",         True,(0,0,0)),(210,180))
    else:
        screen.blit(font.render(f"Деньги:{money} / Бесконечность",True,(0,0,0)),(210,155))
        screen.blit(font.render("Воу ты смог",                    True,(0,0,0)),(210,180))

    screen.blit(font.render("ИИШейдер", True, (0, 0, 0)), (1600, 920))
    if r == 1:
        pygame.draw.rect(screen, (17, 255, 0), (1600, 945, 100, 30))
        screen.blit(font.render("выкл", True, (225,225,225)), (1600, 945))
    else:
        pygame.draw.rect(screen, (255, 0, 0), (1600, 945, 100, 30))
        screen.blit(font.render("вкл", True, (225, 225, 225)), (1600, 945))

    if money < 100 and clicktype == 0:
        screen.blit(bigfont.render("ТЫ ОБАНКРОТИЛСЯ", True, (255,0,0)), (200, 200))
        for _ in range(10):
            screen.blit(bigfont.render("ТЫ ОБАНКРОТИЛСЯ", True, (255, 0, 0)), (200, 200))
            pygame.display.update()
            time.sleep(1)
        money = 100
        f.write(str(money))
        run = False

    if click:
        pos = pygame.mouse.get_pos()
        if 350 <= pos[0] <= 350 + 250 and 600 <= pos[1] <= 600 + 210:
            if clicktype == 1:
                money += 5
            if clicktype == 2:
                money += 30
            if clicktype == 3:
                money += 300
            if clicktype == 4:
                money += 2800
            if clicktype == 5:
                money += 13000
            if clicktype == 6:
                money += 28000

        if r == 0:
            if 775 <= pos[0] <= 875 and 500 <= pos[1] <= 535:
                if money >= 100:
                    money -= 100
                    clicktick = 600
                    clicktype = 1

            if 775 <= pos[0] <= 875 and 550 <= pos[1] <= 585:
                if money >= 1000:
                    money -= 1000
                    clicktick = 665
                    clicktype = 2

            if 775 <= pos[0] <= 875 and 600 <= pos[1] <= 635:
                if money >= 10000:
                    money -= 10000
                    clicktick = 777
                    clicktype = 3

            if 890 <= pos[0] <= 990 and 500 <= pos[1] <= 535:
                if money >= 100000:
                    money -= 100000
                    clicktick = 900
                    clicktype = 4

            if 890 <= pos[0] <= 990 and 550 <= pos[1] <= 585:
                if money >= 500000:
                    money -= 500000
                    clicktick = 1000
                    clicktype = 5

            if 890 <= pos[0] <= 990 and 600 <= pos[1] <= 635:
                if money >= 1000000:
                    money -= 1000000
                    clicktick = 1225
                    clicktype = 6


        else:
            if 775 <= pos[0] <= 875 and 520 <= pos[1] <= 555:
                if money >= 100:
                    money -= 100
                    clicktick = 600
                    clicktype = 1

            if 775 <= pos[0] <= 875 and 570 <= pos[1] <= 605:
                if money >= 1000:
                    money -= 1000
                    clicktick = 665
                    clicktype = 2

            if 775 <= pos[0] <= 875 and 620 <= pos[1] <= 655:
                if money >= 10000:
                    money -= 10000
                    clicktick = 777
                    clicktype = 3

            if 890 <= pos[0] <= 990 and 520 <= pos[1] <= 555:
                if money >= 100000:
                    money -= 100000
                    clicktick = 900
                    clicktype = 4

            if 890 <= pos[0] <= 990 and 570 <= pos[1] <= 605:
                if money >= 500000:
                    money -= 500000
                    clicktick = 1000
                    clicktype = 5

            if 890 <= pos[0] <= 990 and 620 <= pos[1] <= 655:
                if money >= 1000000:
                    money -= 1000000
                    clicktick = 1225
                    clicktype = 6

        if bogat == 1:
            if 1600 <= pos[0] <=  1740 and 155 <= pos[1] <= 190:
                money = 100
                bf.close()
                bf = open(".venv/bogat","w")
                bf.write("0")
                f.close()
                f = open(".venv/money","w")
                f.write(str(money))

        if 1600 <= pos[0] <= 1700 and 945 <= pos[1] <= 975:
            if r == 1:
                rf.close()
                rf = open(".venv/rulist","w")
                r = 0
                rf.write(str(r))
                run = False
            else:
                rf.close()
                rf = open(".venv/rulist","w")
                r = 1
                rf.write(str(r))
                run = False

        if 215 <= pos[0] <= 315 and 950 <= pos[1] <= 985:
            run = False

    if money >= 4000000 and bogat == 0:
        bf.close()
        bogat = 1
        bf = open(".venv/bogat","w")
        money -= 4000000
        money += 100
        f.write(str(money))
        bf.write(str(bogat))
        for _ in range(10):
            screen.blit(bigfont.render(f"ТЫ НАКОПИЛ НА КВАРТИРУ!!1!",True,(242, 255, 0)),(500,300))
            pygame.display.update()
            time.sleep(1)
        run = False

    #автосохранение
    f.close()
    f = open(".venv/money","w")
    f.write(str(money))
    pygame.display.update()
pygame.quit()
