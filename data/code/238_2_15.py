import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.draw.rect(screen, (0, 255, 0), (100, 100, 50, 50))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == '__main__':
    main()