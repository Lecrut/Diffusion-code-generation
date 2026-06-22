from PIL import Image

def render_square_grid(size=256, cell_size=32):
    grid = Image.new('RGB', (size, size), 'white')
    for x in range(0, size, cell_size):
        for y in range(0, size, cell_size):
            draw = ImageDraw.Draw(grid)
            draw.rectangle([x, y, x + cell_size, y + cell_size], outline='black')
    grid.save('square_grid.png')

if __name__ == '__main__':
    render_square_grid()