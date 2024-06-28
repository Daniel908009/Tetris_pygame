import pygame
import random
import time

pygame.init()

def next_piece():
    piece = random.choice(pieces)
    object_parts_from_piece = []
    if piece == "square":
        object_parts_from_piece.append((width/2, height/15))
        object_parts_from_piece.append((width/2 + pixel_size, height/15))
        object_parts_from_piece.append((width/2, height/15 + pixel_size))
        object_parts_from_piece.append((width/2 + pixel_size, height/15 + pixel_size))
    elif piece == "L":
        object_parts_from_piece.append((width/2, height/15))
        object_parts_from_piece.append((width/2, height/15 + pixel_size))
        object_parts_from_piece.append((width/2, height/15 + pixel_size*2))
        object_parts_from_piece.append((width/2 + pixel_size, height/15 + pixel_size*2))
    elif piece == "reverseL":
        object_parts_from_piece.append((width/2 + pixel_size, height/15))
        object_parts_from_piece.append((width/2 + pixel_size, height/15 + pixel_size))
        object_parts_from_piece.append((width/2 + pixel_size, height/15 + pixel_size*2))
        object_parts_from_piece.append((width/2, height/15 + pixel_size*2))
    elif piece == "line":
        object_parts_from_piece.append((width/2, height/15))
        object_parts_from_piece.append((width/2, height/15 + pixel_size))
        object_parts_from_piece.append((width/2, height/15 + pixel_size*2))
        object_parts_from_piece.append((width/2, height/15 + pixel_size*3))
    elif piece == "z":
        object_parts_from_piece.append((width/2, height/15))
        object_parts_from_piece.append((width/2 + pixel_size, height/15))
        object_parts_from_piece.append((width/2 + pixel_size, height/15 + pixel_size))
        object_parts_from_piece.append((width/2 + pixel_size*2, height/15 + pixel_size))
    elif piece == "s":
        object_parts_from_piece.append((width/2 + pixel_size*2, height/15))
        object_parts_from_piece.append((width/2 + pixel_size, height/15))
        object_parts_from_piece.append((width/2 + pixel_size, height/15 + pixel_size))
        object_parts_from_piece.append((width/2, height/15 + pixel_size))
    return object_parts_from_piece

def check_lines():
    for i in range(int((height-height/10)/pixel_size)):
        line = 0
        for j in range(int((width - width/10 - width/10)/pixel_size)):
            if map[i, j] == (255, 255, 255):
                line += 1
        if line == 10:
            remove_line(i)
    
    

def check_collision(object_parts):
    pass

def remove_line():
    pass

def move(object_parts):
    global move_active
    if move_active:
        for i in range(len(object_parts)):
            object_parts[i] = (object_parts[i][0], object_parts[i][1] + pixel_size)
    return object_parts

def pause():
    global move_active
    move_active = False

def rotate():
    pass

def game_over():
    pass

# variables
active = True
speed = 1
pieces = ["square", "L", "reverseL", "line", "z", "s"]
object_parts = []
move_active = True

# screen
height = 800
width = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tetris")
#pygame.display.set_icon(pygame.image.load("Tetris_pygame/tetris.png"))

# grid map
pixel_size = (width - width/10 - width/10) / 10
map = []
for i in range(int((height-height/10)/pixel_size)):
    for j in range(int((width - width/10 - width/10)/pixel_size)):
        map.append((0,0))

# main loop
while active:
    # background
    screen.fill((0, 0, 0))
    # left border
    pygame.draw.rect(screen, (255, 255, 255), (width/10- width/100, height/15, width/100, height - height/10))
    # right border
    pygame.draw.rect(screen, (255, 255, 255), (width- width/10, height/15, width/100, height - height/10))

    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                for part in object_parts:
                    object_parts[part] = list(part)[0] - pixel_size
            if event.key == pygame.K_RIGHT:
                for part in object_parts:
                    part[0] += pixel_size
            if event.key == pygame.K_p:
                pause()

    # draw grid
    for i in range(int((height-height/10)/pixel_size)):
        for j in range(int((width - width/10 - width/10)/pixel_size)):
            pygame.draw.rect(screen, (255, 255, 255), (width/10 + j*pixel_size, height/15 + i*pixel_size, pixel_size, pixel_size), 1)
        
    if object_parts == []:
        object_parts = next_piece()
    else:
        object_parts = move(object_parts)
        #if check_collision(object_parts):
         #   for part in object_parts:
          #      map[part[0], part[1]] = (255, 255, 255)
           # object_parts.clear()
            #check_lines()
            #if game_over():
             #   active = False
        

    # draw object
    for part in object_parts:
        pygame.draw.rect(screen, (255, 255, 255), (part[0], part[1], pixel_size, pixel_size))


    # delay
    time.sleep(speed)

    # update display
    pygame.display.update()



pygame.quit()
