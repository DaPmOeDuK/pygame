from os import path
import random
import pygame
pygame.init()


WIDTH = 600
HEIGHT = 600

FPS = 15

WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (110,180,110)
RED = (255,0,0)
BLACK = (0,0,0)

sound_dir = path.join(path.dirname(__file__),'sound')
pygame.mixer.music.load(path.join(sound_dir,'zastavki.mp3'))

pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('змейка')

clock = pygame.time.Clock()

x1 = HEIGHT//2
y1 = WIDTH//2

y1_ch = 0
x1_ch = 0

long = 1

snake_block = 30

foodx = random.randrange(0,WIDTH - snake_block)
foody = random.randrange(0,HEIGHT - snake_block)

snake_step = 20  #"шаг" объекта в пикселях

snake_list = []

run = True

def food_check(x1,y1,foodx,foody):
    if foodx -snake_block<x1<foodx+snake_block:
        if foody -snake_block<y1<foody+snake_block:
            return True
    else:return False





while run:
    snake_head=[x1,y1]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                y1_ch = 0
                x1_ch = -snake_step

            elif event.key == pygame.K_RIGHT:
                y1_ch = 0
                x1_ch = +snake_step

            elif event.key == pygame.K_UP:
                x1_ch = 0
                y1_ch = -snake_step

            elif event.key == pygame.K_DOWN:
                x1_ch = 0
                y1_ch = +snake_step
            
            elif snake_head[1] > WIDTH or snake_head[0] > HEIGHT or snake_head[1] < 0 or snake_head[0] < 0:
                run = False



    x1 += x1_ch
    y1 += y1_ch            

    screen.fill(GREEN)
    pygame.draw.rect(screen, RED, (foodx, foody,snake_block,snake_block))
    snake_list.append(snake_head)
    #pygame.draw.circle(screen, GREEN, (coord_x, coord_y), 20)
    # pygame.draw.rect(screen, GREEN, (coord_x, coord_y,WIDTH,HEIGHT)) - прямоуг.
    # pygame.draw.polygon(screen, GREEN, (coord_x1, coord_y1,coord_x2, coord_y2,coord_x3, coord_y3,...,coord_x?, coord_y?,)) - многоуг.
    # pygame.draw.line(screen, GREEN, (coord_x(start), coord_y(start)),(coord_x(end), coord_y(end)), WIDTH) - отрезок
    if len(snake_list) > long:
        snake_list.pop(0)
    for i in snake_list:
        pygame.draw.rect(screen, BLACK, (i[0], i[1],snake_block,snake_block))
    if food_check(x1,y1,foodx,foody) == True:
        long+=1
        foodx = random.randrange(0,WIDTH - snake_block)
        foody = random.randrange(0,HEIGHT - snake_block)

    pygame.display.flip()

    clock.tick(FPS)
