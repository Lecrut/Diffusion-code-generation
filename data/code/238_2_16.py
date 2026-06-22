import pygame

def setup_pygame(window_size):
    pygame.init()
    return pygame.display.set_mode(window_size)

def draw_green_rectangle(screen, position, size):
    pygame.draw.rect(screen, (0, 255, 0), (*position, *size))
    pygame.display.flip()

if __name__ == '__main__':
    screen = setup_pygame((200, 200))
    draw_green_rectangle(screen, (100, 100), (50, 50))
    pygame.time.wait(2000)
    pygame.quit()