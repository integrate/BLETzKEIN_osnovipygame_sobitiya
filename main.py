import random

import pygame

pygame.init()

a = pygame.display.set_mode([1400, 700],pygame.NOFRAME)

f = pygame.font.SysFont("arial", 30, True, True)
q = f.render("НЕ ЗАКРОЮСЬ!!", True, [255, 0, 0])
ne = f.render("НЕ СВЕРНУСЬ!!", True, [255, 0, 0])
spaace = f.render("ПрОбЕл", True, [0, 255, 250])
filli = f.render("автоматическая очистка каждые 10 секунд", True, [255, 255, 255])

nomertimer = pygame.event.custom_type()
pygame.time.set_timer(nomertimer, 10000)

while True:
    b = pygame.event.get(pump=False)
    # b = pygame.event.get(pump=False,)
    for u in b:
        print(u)
        if u.type == pygame.QUIT:
            a.blit(q, [650, 300])
        if u.type == 32780 or u.type == 32768:
            a.blit(ne,[700,350])

        if u.type == pygame.KEYDOWN:
            if u.key == pygame.K_SPACE:
                a.blit(spaace, [random.randint(50, 1200), random.randint(50, 650)])
            else:
                keyy = f.render("клавиша " + str(u.key), True, [0, 200, 200])
                a.blit(keyy, [random.randint(50, 1300), random.randint(50, 650)])
        if u.type == pygame.MOUSEBUTTONDOWN:
            if u.button == pygame.BUTTON_LEFT:
                mish = f.render("мышь "+str(u.pos),True,[126,245,72])
                a.blit(mish,u.pos)
            elif u.button == pygame.BUTTON_RIGHT:
                mish = f.render("мышь " + str(u.pos), True, [235, 150, 89])
                a.blit(mish, u.pos)
            else:
                mish = f.render("мышь " + str(u.pos), True, [0, 255, 210])
                a.blit(mish, u.pos)
        if u.type == pygame.MOUSEMOTION:
            # print(u.buttons)
            a.set_at(u.pos,[255,255,255])
            if u.buttons[0] == 1:
                pygame.draw.circle(a, [u.pos[0] / 6, 123, u.pos[1] / 3], u.pos, 20, )
            if u.buttons[1] == 1:
                pygame.draw.circle(a, [u.pos[0] / 6, 123, u.pos[1] / 3], u.pos, 10, )
            if u.buttons[2] == 1:
                pygame.draw.circle(a, [u.pos[0] / 6, 123, u.pos[1] / 3], u.pos, 5, )

        if u.type == nomertimer:
            a.fill([0, 0, 0])
            a.blit(filli, [0, 0])

    pygame.event.pump()
    pygame.display.flip()