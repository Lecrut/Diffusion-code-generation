from PIL import Image

def render_square_grid(size=256, cell_size=None):
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Size must be a positive integer")
    if cell_size is None:
        cell_size = size // 8
    elif not isinstance(cell_size, int) or cell_size <= 0:
        raise ValueError("Cell size must be a positive integer")

    grid = Image.new('RGB', (size, size), 'white')
    draw = grid.load()
    for x in range(0, size, cell_size):
        for y in range(0, size, cell_size):
            if (x // cell_size + y // cell_size) % 2 == 0:
                color = 'black'
            else:
                color = 'white'
            draw.rectangle([x, y, x + cell_size, y + cell_size], fill=color, outline='black')
    grid.save('output.png')

if __name__ == '__main__':
    try:
        render_square_grid(256, 32)
        print("Grid rendered and saved to 'output.png'")
    except ValueError as e:
        print(e)