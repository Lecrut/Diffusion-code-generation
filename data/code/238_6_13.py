import pygame

def create_gray_window():
    try:
        pygame.init()
        screen = pygame.display.set_mode((400, 400))
        gray_color = (128, 128, 128)
        screen.fill(gray_color)
        pygame.display.flip()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        pygame.quit()

if __name__ == '__main__':
    create_gray_window()