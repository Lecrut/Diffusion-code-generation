from PIL import Image

def render_grid():
    grid_size = 10
    cell_size = 32
    size = grid_size * cell_size
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
                    draw[x * cell_size + i, y * cell_size + j] = eval(color)
    image.save('output.png')

if __name__ == '__main__':
    render_grid()