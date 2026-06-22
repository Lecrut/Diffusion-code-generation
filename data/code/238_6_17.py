import pygame

def create_gray_window(size=(400, 400), color=(128, 128, 128)):
    try:
        pygame.init()
        screen = pygame.display.set_mode(size)
        pygame.draw.rect(screen, color, (0, 0, size[0], size[1]))
        pygame.display.update()
        return screen
    except Exception as e:
        print(f"Error creating window: {e}")
        return None

if __name__ == '__main__':
    sample_window = create_gray_window()