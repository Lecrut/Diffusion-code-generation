import pygame

def create_gray_window(width=400, height=400, gray=(128, 128, 128)):
    if not all(isinstance(x, int) for x in [width, height]) or not isinstance(gray, tuple):
        raise ValueError("Invalid dimensions or color format")

    pygame.init()
    window = pygame.display.set_mode((width, height))
    window.fill(gray)
    
    return window

if __name__ == '__main__':
    sample_window = create_gray_window()
    pygame.quit()