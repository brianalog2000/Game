import pygame
import random
pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("Carson's Game")
font = pygame.font.Font('font\Gameplay.ttf', 20)
def menu():
    image=pygame.image.load('assets\menu.png')
    image=pygame.transform.scale(image,(640,480))
    while True:
        screen.blit(image,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(316,337) and event.pos[1] in range(171,205):
                    game()


def game():
    image = pygame.image.load('assets\level1.png')
    image = pygame.transform.scale(image, (640, 480))
    bgx = 0
    player = pygame.image.load('assets\character.png')
    player =pygame.transform.rotozoom(player,0,0.3)
    player_y= 280
    gravity = 1
    jump_count = 0
    jump =0
    jumpsound = pygame.mixer.Sound('assets\jump.mp3')
    crate = pygame.image.load('assets\\bee.png')
    crate = pygame.transform.rotozoom(crate,0,0.3)
    crate_x= 700
    crate_speed=2
    score_value = 0


    while True:
        screen.blit(image, (bgx-640, 0)) #these 3 lines makes the screen scroll
        screen.blit(image, (bgx, 0))
        screen.blit(image, (bgx+640, 0))
#        bgx=bgx-1

        if bgx <= -640:
           bgx=0
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_RIGHT]:
            bgx = bgx - 1
        if keypressed[pygame.K_LEFT]:
            bgx = bgx + 1

        p_rect=screen.blit(player, (50, player_y))
        if player_y < 280:
            player_y += gravity
        if jump == 1:
            player_y = player_y-4
            jump_count += 1
        if jump_count > 40:
            jump_count = 0
            jump = 0
        c_rect=screen.blit(crate, (crate_x, 330))
#        crate_x= random.randint(300, 640)
        crate_x -= crate_speed
        if crate_x<-50:
#            crate_x=700
            crate_x = random.randint(700,820)
            crate_speed = random.randint(2,4)
#        point = c_rect.collidepoint(0, 330)
#        if c_rect.topleft == (0,330):
#            print(c_rect.topleft)
            score_value+=1

        if c_rect.colliderect(p_rect):
            return

#         if event.type==pygame.K_SPACE:
#            print(crate_x)
#        score_value +=1
        text = font.render('Score: ' + str(score_value), True, 'white')
        screen.blit(text, (30,30))

#        else:
#            return



#        if c_rect.colliderect(p_rect):
 #          return

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
#            keypressed = pygame.key.get_pressed()
#            if keypressed[pygame.K_RIGHT]:
#                bgx = bgx - 20
#            if keypressed[pygame.K_LEFT]:
#                bgx = bgx + 20
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
#                    print("jump")
                    jump =1
                    pygame.mixer.Sound.play(jumpsound)
 #                   score_value+=1

#            font = pygame.font.Font('freesansbold.tff', 30)
#            text = font.render('Score: ' + str(score_value), True, 'white')
#            screen.blit(text, (700,30))

menu()


