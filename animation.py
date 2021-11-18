import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the height and withd of the screen

SIZE = [400, 400]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Animation")

# create an empty array
snow_list = []

# add 50 times and add a snow flake in a random x, y position
for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snow_list.append([x, y])

clock = pygame.time.Clock()

# loop until the user clicks the close button
done = False
while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # Set the background
    screen.fill(BLACK)
    
    # Process each snow flake in a list
    for i in range(len(snow_list)):
        
        # Draw the snow flake
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)
        
        # Move the snow flake down one pixel
        snow_list[i][1] += 1
        
        if snow_list[i][1] > 400:
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            
            y = random.randrange(0, 400)
            snow_list[i][0] = y
            
    # Go ahead and update the screen with what we have drawn
    pygame.display.flip()
    clock.tick(20)
    
pygame.quit()
            