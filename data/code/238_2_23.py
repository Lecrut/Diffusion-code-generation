import pygame

def create_window():
    return pygame.display.set_mode((200, 200))

def draw_green_rectangle(screen):
    pygame.draw.rect(screen, (0, 255, 0), (100, 100, 50, 50))
    pygame.display.flip()

if __name__ == '__main__':
    screen = create_window()
    draw_green_rectangle(screen)
    pygame.time.wait(2000)
    pygame.quit()