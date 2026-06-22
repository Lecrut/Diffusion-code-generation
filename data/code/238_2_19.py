import pygame

def create_window():
    return pygame.display.set_mode((400, 400))

def draw_green_rectangle(screen):
    pygame.draw.rect(screen, (0, 255, 0), (150, 150, 100, 100))
    pygame.display.flip()

if __name__ == '__main__':
    screen = create_window()
    draw_green_rectangle(screen)
    pygame.time.wait(3000)
    pygame.quit()