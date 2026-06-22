import pygame

class PygameDrawer:
    SCREEN_SIZE = (200, 200)
    RECTANGLE_POSITION = (100, 100)
    RECTANGLE_SIZE = (50, 50)
    COLOR = (0, 255, 0)

    @staticmethod
    def draw_green_rectangle():
        pygame.init()
        screen = pygame.display.set_mode(PygameDrawer.SCREEN_SIZE)
        pygame.draw.rect(screen, PygameDrawer.COLOR, (*PygameDrawer.RECTANGLE_POSITION, *PygameDrawer.RECTANGLE_SIZE))
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()

if __name__ == '__main__':
    PygameDrawer.draw_green_rectangle()