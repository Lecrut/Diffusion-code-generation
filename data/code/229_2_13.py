from PIL import Image

def render_grid():
    size = 256
    grid_size = 8
    cell_size = size // grid_size
    img = Image.new('RGB', (size, size), color='white')
    draw = ImageDraw.Draw(img)
    
    for i in range(1, grid_size):
        x = i * cell_size
        y = i * cell_size
        draw.line([(x, 0), (x, size)], fill='black')
        draw.line([(0, y), (size, y)], fill='black')
    
    img.save('grid.png')

if __name__ == '__main__':
    render_grid()