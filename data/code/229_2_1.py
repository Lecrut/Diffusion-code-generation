from PIL import Image

def render_grid():
    size = 256
    grid_size = 8
    cell_size = size // grid_size
    image = Image.new('RGB', (size, size), 'white')
    draw = image.load()
    
    for x in range(grid_size):
        for y in range(grid_size):
            if (x + y) % 2 == 0:
                color = 'black'
            else:
                color = 'white'
            for i in range(cell_size):
                for j in range(cell_size):
                    draw[x * cell_size + i, y * cell_size + j] = color
    
    image.save('grid.png')

if __name__ == '__main__':
    render_grid()