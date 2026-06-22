from PIL import Image

def render_square_grid(size=200, cell_size=50):
    grid = Image.new('RGB', (size, size), color='white')
    draw = ImageDraw.Draw(grid)
    
    for i in range(1, size // cell_size):
        draw.line((i * cell_size, 0, i * cell_size, size), fill='black')
        draw.line((0, i * cell_size, size, i * cell_size), fill='black')
    
    grid.save('output.png')

if __name__ == '__main__':
    render_square_grid()