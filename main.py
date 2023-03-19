import pygame
import random

# initialize pygame
pygame.init()

# set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong Game")

# set up the game objects
paddle_width = 20
paddle_height = 100
paddle_speed = 5
player1_pos = pygame.Rect(50, 250, paddle_width, paddle_height)
player2_pos = pygame.Rect(730, 250, paddle_width, paddle_height)
ball_pos = pygame.Rect(WINDOW_WIDTH/2-10, WINDOW_HEIGHT/2-10, 20, 20)
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5 * random.choice((1, -1))

# set up the game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_pos.top > 0:
        player1_pos.move_ip(0, -paddle_speed)
    if keys[pygame.K_s] and player1_pos.bottom < WINDOW_HEIGHT:
        player1_pos.move_ip(0, paddle_speed)
    if keys[pygame.K_UP] and player2_pos.top > 0:
        player2_pos.move_ip(0, -paddle_speed)
    if keys[pygame.K_DOWN] and player2_pos.bottom < WINDOW_HEIGHT:
        player2_pos.move_ip(0, paddle_speed)

    # update the game state
    ball_pos.move_ip(ball_speed_x, ball_speed_y)

    # check for collision with walls and paddles
    if ball_pos.left < 0 or ball_pos.right > WINDOW_WIDTH:
        ball_speed_x *= -1
    if ball_pos.top < 0 or ball_pos.bottom > WINDOW_HEIGHT:
        ball_speed_y *= -1
    if ball_pos.colliderect(player1_pos) or ball_pos.colliderect(player2_pos):
        ball_speed_x *= -1

    # draw the game objects
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), player1_pos)
    pygame.draw.rect(screen, (0, 0, 0), player2_pos)
    pygame.draw.ellipse(screen, (0, 0, 0), ball_pos)
    pygame.display.flip()

    # set the frame rate
    clock = pygame.time.Clock()
