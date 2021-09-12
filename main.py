
import pygame

pygame.init()

screen = pygame.display.set_mode((1600, 900))

pygame.display.set_caption('Pingu Gayme')
icon = pygame.image.load(r"pictures/penguin_icon.png")
pygame.display.set_icon(icon)

player_stage1_Img = pygame.image.load(r"pictures/penguin_transformed_1.png")
player_stage2_Img = pygame.image.load(r"pictures/penguin_transformed_2.png")
player_stage3_Img = pygame.image.load(r"pictures/penguin_transformed_3.png")
PlayerX = 800
PlayerY = 300
PlayerX_change = 0
PlayerY_change = 0
transformed = 0
mirrored = True
Facing_right = True
R_down = None
L_down = None


def player(xval, yval):
    if Facing_right == True:
        if transformed == 0:
            screen.blit(player_stage1_Img, (xval, yval))
        elif transformed == 1:
            screen.blit(player_stage2_Img, (xval, yval))
        elif transformed == 2:
            screen.blit(player_stage3_Img, (xval, yval))
    elif Facing_right == False:
        if transformed == 0:
            screen.blit(pygame.transform.flip(
                player_stage1_Img, True, False), (xval, yval))
        elif transformed == 1:
            screen.blit(pygame.transform.flip(
                player_stage2_Img, True, False), (xval, yval))
        elif transformed == 2:
            screen.blit(pygame.transform.flip(
                player_stage3_Img, True, False), (xval, yval))


running = True
while running:
    if mirrored == True:
        screen.fill((162, 210, 223))
    else:
        screen.fill((128, 149, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            if L_down != True:
                if event.key == pygame.K_d:
                    PlayerX_change = 0.3
                    Facing_right = True
            if R_down != True:
                if event.key == pygame.K_a:
                    PlayerX_change = -0.3
                    Facing_right = False
            if event.key == pygame.K_s:
                PlayerY_change = 0.3
            if event.key == pygame.K_w:
                PlayerY_change = -0.3
            if event.key == pygame.K_LSHIFT:
                if transformed >= 2:
                    transformed = 0
                else:
                    transformed += 1
            if event.key == pygame.K_SPACE:
                mirrored = not mirrored
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                PlayerX_change = 0
            if event.key == pygame.K_a:
                PlayerX_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                PlayerY_change = 0
            if event.key == pygame.K_LSHIFT:
                transformed = transformed
    if transformed == 0:
        PlayerX += PlayerX_change
        PlayerY += PlayerY_change
    elif transformed == 1:
        PlayerX += PlayerX_change * 2
        PlayerY += PlayerY_change * 2
    elif transformed == 2:
        PlayerX += PlayerX_change * 3
        PlayerY += PlayerY_change * 3
    if PlayerX >= 1600:
        PlayerX = -50
    elif PlayerX <= -50:
        PlayerX = 1600
    if PlayerY >= 900:
        PlayerY = -70
    elif PlayerY <= -70:
        PlayerY = 900
    player(PlayerX, PlayerY)
    pygame.display.update()
