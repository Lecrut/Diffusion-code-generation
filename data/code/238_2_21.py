import pygame

class PygameRenderer:
    WINDOW_SIZE = (200, 200)
    RECTANGLE_POSITION = (100, 100)
    RECTANGLE_SIZE = (50, 50)
    COLOR = (0, 255, 0)

    @staticmethod
    def draw_green_rectangle():
        pygame.init()
        screen = pygame.display.set_mode(PygameRenderer.WINDOW_SIZE)
        pygame.draw.rect(screen, PygameRenderer.COLOR, (*PygameRenderer.RECTANGLE_POSITION, *PygameRenderer.RECTANGLE_SIZE))
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()

if __name__ == '__main__':
    PygameRenderer.draw_green_rectangle()