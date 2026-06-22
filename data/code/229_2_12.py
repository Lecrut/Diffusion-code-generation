from PIL import Image
GRID_SIZE = 8
CELL_SIZE = GRID_SIZE * GRID_SIZE
IMAGE_SIZE = (CELL_SIZE, CELL_SIZE)

def render_square_grid():
    image = Image.new('RGB', IMAGE_SIZE, 'white')
    draw = image.load()
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if (i + j) % 2 == 0:
                color = 'black'
            else:
                color = 'white'
            draw[i * CELL_SIZE // GRID_SIZE, j * CELL_SIZE // GRID_SIZE] = color
    image.save('square_grid.png')
if __name__ == '__main__':
    render_square_grid()