from PIL import Image

GRID_SIZE = 8
CELL_SIZE = GRID_SIZE * GRID_SIZE
BACKGROUND_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)

def render_square_grid():
    image = Image.new('RGB', (CELL_SIZE, CELL_SIZE), BACKGROUND_COLOR)
    draw = image.load()
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if (x + y) % 2 == 0:
                draw[x * GRID_SIZE, y * GRID_SIZE] = LINE_COLOR
    image.save('square_grid.png')

if __name__ == '__main__':
    render_square_grid()