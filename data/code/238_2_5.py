import pygame

def draw_green_rectangle():
    settings = {
        'window_size': (200, 200),
        'rectangle_position': (100, 100),
        'rectangle_size': (50, 50),
        'color': (0, 255, 0)
    }
    
    pygame.init()
    screen = pygame.display.set_mode(settings['window_size'])
    pygame.draw.rect(screen, settings['color'], (*settings['rectangle_position'], *settings['rectangle_size']))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()

if __name__ == '__main__':
    draw_green_rectangle()