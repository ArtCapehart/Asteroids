# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        screen.fill((0, 0, 0))  # Fill the screen with black
        pygame.display.flip()   # Refresh the screen

        for event in pygame.event.get():  # Make sure this line is indented with 4 spaces
            if event.type == pygame.QUIT:
                return  # This exits the loop & closes the program

if __name__ == "__main__":
    main()
