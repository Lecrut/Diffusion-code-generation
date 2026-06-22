from PIL import Image

def render_square_grid(size=256, cell_size=None):
    if size <= 0:
        raise ValueError("Size must be greater than zero.")
    if cell_size is None:
        cell_size = size // 8
    elif cell_size <= 0 or cell_size > size:
        raise ValueError("Cell size must be between 1 and size.")

    grid = Image.new('RGB', (size, size), 'white')
    draw = grid.load()
    
    for x in range(0, size, cell_size):
        for y in range(0, size, cell_size):
            if (x // cell_size + y // cell_size) % 2 == 0:
                color = 'black'
            else:
                color = 'white'
            draw.rectangle([x, y, x + cell_size, y + cell_size], fill=color)

    grid.save('square_grid.png')

if __name__ == '__main__':
    render_square_grid()