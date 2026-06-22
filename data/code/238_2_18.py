import pygame
WINDOW_SIZE = (200, 200)
RECTANGLE_POSITION = (100, 100)
RECTANGLE_SIZE = (50, 50)
COLOR_GREEN = (0, 255, 0)

def draw_green_rectangle():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.draw.rect(screen, COLOR_GREEN, RECTANGLE_POSITION + RECTANGLE_SIZE)
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
if __name__ == '__main__':
    draw_green_rectangle()