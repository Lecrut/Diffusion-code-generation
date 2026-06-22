import pygame

class PygameWindow:

    def __init__(self, width=400, height=400):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Gray Window')

    def fill_gray(self):
        gray_color = (128, 128, 128)
        self.screen.fill(gray_color)

    def update(self):
        pygame.display.flip()

    def quit(self):
        pygame.quit()
if __name__ == '__main__':
    window = PygameWindow()
    window.fill_gray()
    window.update()
    pygame.time.delay(2000)
    window.quit()