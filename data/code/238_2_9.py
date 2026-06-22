import pygame

def init_window(size):
    if not isinstance(size, tuple) or len(size) != 2:
        raise ValueError("Window size must be a tuple of two integers")
    return pygame.display.set_mode(size)

def draw_green_rectangle(screen, position, size, color):
    if not (isinstance(screen, pygame.Surface) and 
            isinstance(position, tuple) and len(position) == 2 and 
            isinstance(size, tuple) and len(size) == 2 and 
            isinstance(color, tuple) and len(color) == 3):
        raise ValueError("Invalid parameters for drawing rectangle")
    pygame.draw.rect(screen, color, (*position, *size))
    pygame.display.flip()

if __name__ == '__main__':
    try:
        window_size = (200, 200)
        screen = init_window(window_size)
        draw_green_rectangle(screen, (100, 100), (50, 50), (0, 255, 0))
        pygame.time.wait(2000)
    finally:
        pygame.quit()