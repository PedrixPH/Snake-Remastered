import pygame
import random


# Inicializando Pygame
pygame.init()

# Cores
COLOR_BLUE = (93, 143, 222)
COLOR_GREEN = (17, 105, 10)
COLOR_RED = (212, 13, 13)

# Tela
window = (1280, 720)
screen = pygame.display.set_mode(window)

#Relógio do jogo
game_clock = pygame.time.Clock()

def img(snake_head):
    img_path = "./assets/snake/"+snake_head+".png"
    return pygame.image.load(img_path).convert_alpha()

def rotated_img(angle, snake_head_img):
    return pygame.transform.rotate(snake_head_img, angle)

# Loop Principal
def game_loop():
    # Snake Propriedades
    snake_head_img = img("snake_head")
    snake_head = snake_head_img.get_rect()
    snake_head_pos = (window[0] // 2, window[1] // 2)
    snake_size = snake_head.width
    delta_x = 0
    delta_y = 0

    #Snake_Body
    snake_body_img = img("snake_body")
    snake_body_positions = [snake_head_pos]
    snake_length = 1

    # Fruit
    fruit_pos = (random.randrange(window[0] // snake_size)*snake_size, random.randrange(window[1]//snake_size)*snake_size)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and delta_x != -snake_size:
                    if delta_y <= 0 and delta_x == 0:
                        snake_head_img = rotated_img(-90, snake_head_img)
                    elif delta_y > 0:
                        snake_head_img = rotated_img(90, snake_head_img)
                    delta_y = 0
                    delta_x = snake_size
                elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and delta_x != snake_size:
                    if delta_y <= 0 and delta_x == 0:
                        snake_head_img = rotated_img(90, snake_head_img)
                    elif delta_y > 0:
                        snake_head_img = rotated_img(-90, snake_head_img)
                    delta_y = 0
                    delta_x = -snake_size
                elif (event.key == pygame.K_w or event.key == pygame.K_UP) and delta_y != snake_size:
                    if delta_x > 0 and delta_y == 0:
                        snake_head_img = rotated_img(90, snake_head_img)
                    elif delta_x < 0:
                        snake_head_img = rotated_img(-90, snake_head_img)
                    delta_y = -snake_size
                    delta_x = 0
                elif (event.key == pygame.K_s or event.key == pygame.K_DOWN) and delta_y != -snake_size:
                    if delta_x > 0 and delta_y == 0:
                        snake_head_img = rotated_img(-90, snake_head_img)
                    elif delta_x < 0:
                        snake_head_img = rotated_img(90, snake_head_img)
                    elif delta_y == 0 and delta_x ==0:
                        snake_head_img = rotated_img(180, snake_head_img)
                    delta_y = snake_size
                    delta_x = 0
        #Snake head move
        snake_head_pos = (snake_head_pos[0]+delta_x, snake_head_pos[1]+delta_y)
        snake_body_positions.insert(0, snake_head_pos)

        #Snake body move
        if len(snake_body_positions) > snake_length:
            del snake_body_positions[len(snake_body_positions)-1]

        game_clock.tick(10)
        pygame.time.delay(150)

        screen.fill(COLOR_BLUE)

        #Snake eat fruit
        if fruit_pos == snake_head_pos:
            snake_length += 1
            fruit_pos = (random.randrange(window[0] // snake_size)*snake_size,
                         random.randrange(window[1] // snake_size)*snake_size)

        if snake_head_pos[0] >= window[0]-snake_size:
            snake_head_pos = (-snake_size, snake_head_pos[1])
        elif snake_head_pos[0] < 0:
            snake_head_pos = (window[0], snake_head_pos[1])
        if snake_head_pos[1] >= window[1]-snake_size:
            snake_head_pos = (snake_head_pos[0], -snake_size)
        elif snake_head_pos[1] < 0:
            snake_head_pos = (snake_head_pos[0], window[1])

        #Desenhar a cobra
        for i in range(len(snake_body_positions)):
            if i == 0:
                screen.blit(snake_head_img, snake_body_positions[i])
            else:
                screen.blit(snake_body_img, snake_body_positions[i])

        #Desenhar a fruta
        pygame.draw.rect(screen, COLOR_RED, (fruit_pos[0], fruit_pos[1], snake_size, snake_size))

        pygame.display.update()

game_loop()
