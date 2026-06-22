import pygame

def create_gray_window():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    screen.fill((128, 128, 128))
    pygame.display.update()

if __name__ == '__main__':
    create_gray_window()