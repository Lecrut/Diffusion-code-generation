from PIL import Image

def render_square_grid():
    size = 200
    grid_size = 10
    cell_size = size // grid_size
    image = Image.new('RGB', (size, size), 'white')
    draw = image.draw()
    
    for i in range(grid_size):
        for j in range(grid_size):
            x1, y1 = i * cell_size, j * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            draw.rectangle([x1, y1, x2, y2], outline='black')
    
    image.save('square_grid.png')

if __name__ == '__main__':
    render_square_grid()