import pygame
import random
import time
pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale(pygame.image.load("Space image.jpg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VEL = 5

ASTEROID_WIDTH = 10
ASTEROID_HEIGHT = 20

ASTEROID_VEL = 3

FONT = pygame.font.SysFont("comicans", 30)

def draw(player, elapsed_time, asteroids):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))
    
    pygame.draw.rect(WIN, (255, 0, 0), player)

    for asteroid in asteroids:
        pygame.draw.rect(WIN, "white", asteroid)
    
    pygame.display.update()

    

def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    asteroid_add_increment = 2000
    asteroid_count = 0

    asteroids = []

    hit = False


    while run:
        asteroid_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if asteroid_count > asteroid_add_increment:
            for _ in range(3):
                asteroid_x = random.randint(0, WIDTH - ASTEROID_WIDTH)
                asteroid = pygame.Rect(asteroid_x, -ASTEROID_HEIGHT, ASTEROID_WIDTH, ASTEROID_HEIGHT)
                asteroids.append(asteroid)

            asteroid_add_increment = max(200, asteroid_add_increment - 50)
            asteroid_count = 0
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        for asteroid in asteroids[:]:
            asteroid.y += ASTEROID_VEL
            if asteroid.y > HEIGHT:
                asteroids.remove(asteroid)
            elif asteroid.y + asteroid.height >= player.y and asteroid.colliderect(player):
                asteroids.remove(asteroid)
                hit = True
                break
        
        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break
        
        draw(player, elapsed_time, asteroids)

    pygame.QUIT()


if __name__ == "__main__":
    main()