import pygame
import random

class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 20
        self.direction = "right"

    def update(self):
        # Získání stisknutých kláves
        keys = pygame.key.get_pressed()

        # Nastavení směru hada podle stisknutých kláves
        if keys[pygame.K_w]:
            self.direction = "up"
        elif keys[pygame.K_a]:
            self.direction = "left"
        elif keys[pygame.K_s]:
            self.direction = "down"
        elif keys[pygame.K_d]:
            self.direction = "right"

        # Pohyb hada podle směru
        if self.direction == "right":
            self.rect.x += self.speed
        elif self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "up":
            self.rect.y -= self.speed
        elif self.direction == "down":
            self.rect.y += self.speed

        # Kontrola okraje obrazovky
        if self.rect.x < 0:
            self.rect.x = 780
        elif self.rect.x > 800:
            self.rect.x = 0
        elif self.rect.y < 0:
            self.rect.y = 580
        elif self.rect.y > 600:
            self.rect.y = 0

class Food(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.reset()

    def reset(self):
        self.rect.x = random.randint(0, self.screen_width - 20)
        self.rect.y = random.randint(0, self.screen_height - 20)

# Inicializace Pygame
pygame.init()

# Vytvoření okna o velikosti 800x600
screen = pygame.display.set_mode((800, 600))

# Nastavení titulku okna
pygame.display.set_caption("Hra Snake")

# Vytvoření objektu hada
snake = Snake(400, 300)

# Vytvoření objektu jídla
food = Food(800,600)

# Hlavní herní smyčka
running = True
while running:
    # Zpracování událostí
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Aktualizace herního stavu
    snake.update()

    # Kontrola, zda had sežral jídlo
    if snake.rect.colliderect(food.rect):
        # Náhodné umístění nového kousku jídla
        food.rect.x = random.randint(0, 780)
        food.rect.y = random.randint(0, 580)

    # Vyčištění obrazovky
    screen.fill((0, 0, 0))

    # Vykreslení hada
    screen.blit(snake.image, snake.rect)

    # Vykreslení jídla
    pygame.draw.rect(screen, (255, 0, 0), food.rect)

    # Aktualizace obrazovky
    pygame.display.flip()

    # Zpoždění
    pygame.time.delay(100)

# Ukončení Pygame
pygame.quit()
