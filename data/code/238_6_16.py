import pygame

def fill_gray(surface):
    surface.fill((128, 128, 128))

if __name__ == '__main__':
    screen = pygame.display.set_mode((400, 400))
    fill_gray(screen)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()