from PIL import Image

def render_square_grid():
    grid_size = 4
    cell_size = 50
    image = Image.new('RGB', (grid_size * cell_size, grid_size * cell_size), 'white')
    draw = image.load()
    for i in range(grid_size):
        for j in range(grid_size):
            color = 'black' if (i + j) % 2 == 0 else 'white'
            x1, y1 = i * cell_size, j * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            draw.rectangle([x1, y1, x2, y2], fill=color)
    image.save('output.png')

if __name__ == '__main__':
    render_square_grid()