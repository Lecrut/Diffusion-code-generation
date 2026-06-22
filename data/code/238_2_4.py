import pygame

def draw_green_rectangle():
    pygame.init()
    screen = pygame.display.set_mode((200, 200))
    pygame.draw.rect(screen, (0, 255, 0), (100, 100, 50, 50))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()

if __name__ == '__main__':
    draw_green_rectangle()