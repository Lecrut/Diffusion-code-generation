import pygame

def create_window(size):
    return pygame.display.set_mode(size)

def draw_green_rectangle(screen, position, size, color):
    pygame.draw.rect(screen, color, (*position, *size))

def main():
    window_size = (200, 200)
    rectangle_position = (100, 100)
    rectangle_size = (50, 50)
    rectangle_color = (0, 255, 0)

    pygame.init()
    screen = create_window(window_size)
    
    draw_green_rectangle(screen, rectangle_position, rectangle_size, rectangle_color)
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()

if __name__ == '__main__':
    main()