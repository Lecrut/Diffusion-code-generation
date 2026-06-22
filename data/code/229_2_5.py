from PIL import Image

def render_grid():
    size = 256
    grid_size = 8
    cell_size = size // grid_size
    
    image = Image.new('RGB', (size, size), 'white')
    draw = image.load()
    
    for i in range(grid_size):
        for j in range(grid_size):
            if (i + j) % 2 == 0:
                color = 'black'
            else:
                color = 'white'
            for x in range(cell_size * i, cell_size * (i + 1)):
                for y in range(cell_size * j, cell_size * (j + 1)):
                    draw[x, y] = color
    
    image.save('output.png')

if __name__ == '__main__':
    render_grid()