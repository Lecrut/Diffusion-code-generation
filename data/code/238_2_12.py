import pygame

class Graphics:
    def __init__(self):
        self.width = 200
        self.height = 200
        self.rect_x = 100
        self.rect_y = 100
        self.rect_width = 50
        self.rect_height = 50
        self.color = (0, 255, 0)

    def init_pygame(self):
        pygame.init()
        return pygame.display.set_mode((self.width, self.height))

    def draw_rectangle(self, screen):
        pygame.draw.rect(screen, self.color, (self.rect_x, self.rect_y, self.rect_width, self.rect_height))
        pygame.display.flip()

if __name__ == '__main__':
    graphics = Graphics()
    screen = graphics.init_pygame()
    graphics.draw_rectangle(screen)
    pygame.time.wait(2000)
    pygame.quit()