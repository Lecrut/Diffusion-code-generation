import pygame

def init_pygame():
    pygame.init()
    return pygame.display.set_mode((200, 200))

def draw_rectangle(screen):
    pygame.draw.rect(screen, (0, 255, 0), (100, 100, 50, 50))
    pygame.display.flip()

if __name__ == '__main__':
    screen = init_pygame()
    draw_rectangle(screen)
    pygame.time.wait(2000)
    pygame.quit()