import random
import time
import pygame
from pygame import (
    K_LEFT,
    K_RIGHT,
    K_SPACE
)

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500


class Arrear(pygame.sprite.Sprite):
    SPEED = 1
    SIZE = 1

    def __init__(self):
        super(Arrear, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((255, 255, 0))  # Change appearance
        self.rect = self.surf.get_rect(center=(random.randint(0, SCREEN_WIDTH), 0))

    def move(self):
        self.rect.move_ip(0, Arrear.SPEED)


class Player(pygame.sprite.Sprite):
    SPEED = 1
    SIZE = 30

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((Player.SIZE, Player.SIZE))
        self.surf.fill((255, 255, 255))  # Change appearance
        self.rect = self.surf.get_rect(center=(
            SCREEN_WIDTH,
            SCREEN_HEIGHT
        ))

    def update(self, keys):
        if keys[K_LEFT]:
            self.rect.move_ip(-Player.SPEED, 0)
        elif keys[K_RIGHT]:
            self.rect.move_ip(Player.SPEED, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


pygame.init()

running = True

screen = pygame.display.set_mode((500, 500))

player = Player()
arrears = []

counter = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()

    if counter > 1000:
        arrears.append(Arrear())
        counter = 0

    for arrear in arrears:
        arrear.move()
        screen.blit(arrear.surf, arrear.rect)

    player.update(pressed_keys)
    screen.blit(player.surf, player.rect)

    pygame.display.flip()

    screen.fill((0, 0, 0))

    counter += 1

    #time.sleep(1)
