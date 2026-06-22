import pygame

def setup_pygame(size):
    pygame.init()
    return pygame.display.set_mode(size)

def draw_green_rectangle(screen, position, size, color):
    pygame.draw.rect(screen, color, (*position, *size))
    pygame.display.flip()

if __name__ == '__main__':
    settings = {
        'window_size': (200, 200),
        'rectangle_position': (100, 100),
        'rectangle_size': (50, 50),
        'color': (0, 255, 0)
    }
    screen = setup_pygame(settings['window_size'])
    draw_green_rectangle(screen, settings['rectangle_position'], settings['rectangle_size'], settings['color'])
    pygame.time.wait(2000)
    pygame.quit()