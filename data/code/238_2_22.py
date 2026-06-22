import pygame

def create_window(size):
    return pygame.display.set_mode(size)

def draw_green_rectangle(screen, position, size):
    pygame.draw.rect(screen, (0, 255, 0), (position[0], position[1], size[0], size[1]))

if __name__ == '__main__':
    window_size = (400, 300)
    rectangle_position = (150, 100)
    rectangle_size = (75, 60)

    pygame.init()
    screen = create_window(window_size)
    draw_green_rectangle(screen, rectangle_position, rectangle_size)
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()