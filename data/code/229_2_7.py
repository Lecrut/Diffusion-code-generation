from PIL import Image

def render_grid(size=200, cell_size=50):
    grid = Image.new('RGB', (size, size), color='white')
    draw = ImageDraw.Draw(grid)
    for x in range(0, size, cell_size):
        draw.line([(x, 0), (x, size)], fill='black')
    for y in range(0, size, cell_size):
        draw.line([(0, y), (size, y)], fill='black')
    grid.save('output.png')

if __name__ == '__main__':
    render_grid()