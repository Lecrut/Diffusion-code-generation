import pygame

def create_window(size):
    try:
        return pygame.display.set_mode(size)
    except Exception as e:
        print(f"Error creating window: {e}")
        return None

def draw_green_rectangle(screen, position, size):
    if screen is not None:
        pygame.draw.rect(screen, (0, 255, 0), (*position, *size))
        pygame.display.flip()
    else:
        print("Window must be initialized before drawing.")

if __name__ == '__main__':
    window_size = (200, 200)
    rectangle_position = (100, 100)
    rectangle_size = (50, 50)

    screen = create_window(window_size)
    draw_green_rectangle(screen, rectangle_position, rectangle_size)
    pygame.time.wait(2000)
    pygame.quit()