import pygame

def create_window(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive integers.")
    
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    return screen

def fill_screen(screen, color):
    if not isinstance(color, tuple) or len(color) != 3:
        raise ValueError("Color must be a tuple of three integers.")
    
    screen.fill(color)

if __name__ == '__main__':
    sample_width = 400
    sample_height = 400
    gray_color = (128, 128, 128)
    
    window = create_window(sample_width, sample_height)
    fill_screen(window, gray_color)
    
    pygame.quit()