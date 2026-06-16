# Example file showing a circle moving on screen
import pygame
import random
import time


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
speed = 1
max_energy = 1000
energy = 1000
player_pos = pygame.Vector2(screen.get_width() / 5 , screen.get_height() / 2)
enemy_pos = pygame.Rect(screen.get_width(), random.randint (0, screen.get_height()), 30 , 30)
enemy1_pos = pygame.Rect(screen.get_width() - 30, random.randint (0, screen.get_height()), 30, 30)
enemy2_pos = pygame.Rect(screen.get_width() - 30, random.randint (0, screen.get_height()), 30, 30)
is_shooting = False
beam_rect = pygame.Rect(player_pos.x, player_pos.y, 1280, 40)
enemy_lives = 5
enemy_max_lives = 5
winner = 0
Raider_vertical = 1
Raider_horizontal = 1
guardian_speed = 1
charge_speed = 1
death_frames = 0
secret_frames = 0
secret_frames_used = False
death_frames_2 = 0
sleep = 1

raider1immage = pygame.image.load("raider_balloon.png")


def draw_energy_bar():                               
    energyBarHeight = (energy) /max_energy   * screen.get_height()
    pygame.draw.rect(screen, (128, 255, 0), pygame.Rect(0 , screen.get_height() - energyBarHeight, 40 , energyBarHeight))
    pygame.draw.rect(screen, "blue", pygame.Rect(0 , screen.get_height() - (300/max_energy * screen.get_height() ) , 60 , 10  ))
    pygame.draw.rect(screen, (128, 255, 0), pygame.Rect(0 , screen.get_height() - (200/max_energy * screen.get_height() ) , 60 , 10  ))
    pygame.draw.rect(screen, (128, 255, 0), pygame.Rect(0 , screen.get_height() - (100/max_energy * screen.get_height() ) , 60 , 10  ))
    pygame.draw.rect(screen, (128, 255, 0), pygame.Rect(0 , screen.get_height() - (400/max_energy * screen.get_height() ) , 60 , 10  ))
    for i in range (5, 10):
            pygame.draw.rect(screen, (128, 255, 0), pygame.Rect(0 , screen.get_height() - (100 * i /max_energy * screen.get_height() ) , 60 , 10  ))
    enemyLivesBarHeight = screen.get_height() * (enemy_lives / enemy_max_lives)
    pygame.draw.rect(screen, pygame.Color(127, 0, 255), pygame.Rect(screen.get_width() -  40, screen.get_height() - enemyLivesBarHeight, 40, enemyLivesBarHeight))
    # dark green
def draw_entities():
    global secret_frames
    pygame.draw.circle(screen, pygame.Color(128,255,0), player_pos, 40)
    if secret_frames > 0:
        pygame.draw.rect(screen, pygame.Color(127, 0, 255), pygame.Rect(enemy_pos.x, enemy_pos.y, 200, enemy_pos.h))
        secret_frames -= 1
    else:
        #pygame.draw.rect(screen, pygame.Color(127, 0, 255), enemy_pos)
        screen.blit(raider1immage,enemy_pos)
    pygame.draw.rect(screen, pygame.Color(255, 200, 60), enemy1_pos)
    pygame.draw.rect(screen, pygame.Color(255, 200, 60), enemy2_pos)
    pygame.draw.rect(screen, pygame.Color("white"), beam_prepare, 5)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if winner == 0:
        if death_frames > 7 :
               screen.fill("white")
        elif death_frames > 0 :
            screen.fill("yellow")
        elif death_frames_2 > 7:
            screen.fill("pink")
        elif death_frames_2 > 7:
            screen.fill(255, 200, 60)
        else:
            screen.fill((0,255,255))
    if winner == -1:
        screen.fill((127 , 0 , 255))
    if winner == 1:
        screen.fill((128, 255, 0))

    if winner == 0 :
        beam_prepare = pygame.Rect(player_pos.x, player_pos.y - 20 , 1280, 40)
        draw_entities()
        enemy_pos.x = enemy_pos.x - 100 * dt * Raider_horizontal
        enemy1_pos.x = enemy1_pos.x - 50 * dt * Raider_horizontal
        enemy2_pos.x = enemy2_pos.x - 50 * dt * Raider_horizontal
        if enemy_pos.y - enemy_pos.h < 0:
            enemy_pos.y = screen.get_height() - 31
        if enemy_pos.y + enemy_pos.h > screen.get_height():
            enemy_pos.y = 31
            
        if player_pos.y + player_pos.x < 0:
            player_pos.y = screen.get_height()
        if player_pos.y > screen.get_height():
            player_pos.y = 0
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if not secret_frames_used:
                secret_frames_used = True
                enemy_pos.x -= 200
                enemy_pos.y = random.randint(0, screen.get_height())
                secret_tunnel = 0
                secret_frames = 15
        if keys[pygame.K_UP]:
            enemy_pos.y -= 500 * dt * Raider_vertical
        if keys[pygame.K_DOWN]:
                enemy_pos.y += 500 * dt * Raider_vertical 
        if keys[pygame.K_RIGHT]:
            enemy_pos.x += 100 * dt * Raider_vertical 
        if keys[pygame.K_w]:
            if is_shooting == False:
                player_pos.y -= 600 * dt 
            else:
                player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            if is_shooting == False:
                player_pos.y += 600 * dt
            else :
                player_pos.y += 300 * dt
        if keys[pygame.K_SPACE]:
            if energy >= 300 or is_shooting == True:
                if energy > 0:
                    beam_rect = pygame.Rect(player_pos.x, player_pos.y - 20 , 1280, 40)
                    pygame.draw.rect(screen, (128, 255, 0), beam_rect)
                    energy = energy - 1000 * dt
                    is_shooting = True
                else:
                    is_shooting = False
            else:
                is_shooting = False
        else:
            is_shooting = False

        if is_shooting == False and energy <= 1000:
            energy = energy + 10 * charge_speed
        if not is_shooting:
            beam_rect = pygame.Rect(0, 0, 0, 0)
        if enemy1_pos.colliderect(beam_rect):
            enemy1_pos.x = 1000
            enemy1_pos.y = random.randint(31, screen.get_height() - 31)
            death_frames_2 = 15
        if enemy2_pos.colliderect(beam_rect):
            enemy2_pos.x = 1000
            enemy2_pos.y = random.randint(31, screen.get_height() - 31)
            death_frames_2 = 15
        if enemy_pos.x < 0 or enemy1_pos.x < 0 or enemy2_pos.x < 0:
            winner = -1
        if enemy_pos.colliderect(beam_rect):
            enemy_pos.x = 1000
            enemy_pos.y = random.randint(0, screen.get_height())
            enemy_lives = enemy_lives - 1
            death_frames = 15
            enemy2_pos.x = 1000
            secret_frames_used = False
            if enemy_lives < 1:
                winner = 1
        if enemy_pos.x < 0:
            winner = -1
        death_frames_2 -= 1
        draw_energy_bar()
    death_frames = death_frames - 1
    sleep -= 1  
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
