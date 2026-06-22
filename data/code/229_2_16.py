from PIL import Image

class GridRenderer:
    SIZE = 256
    CELL_SIZE = 16

    @staticmethod
    def render_grid():
        image = Image.new('RGB', (GridRenderer.SIZE, GridRenderer.SIZE), 'white')
        draw = image.load()
        for x in range(0, GridRenderer.SIZE, GridRenderer.CELL_SIZE):
            for y in range(0, GridRenderer.SIZE, GridRenderer.CELL_SIZE):
                if (x // GridRenderer.CELL_SIZE + y // GridRenderer.CELL_SIZE) % 2 == 0:
                    color = 'black'
                else:
                    color = 'white'
                for i in range(GridRenderer.CELL_SIZE):
                    for j in range(GridRenderer.CELL_SIZE):
                        draw[x + i, y + j] = eval(color)
        image.save('grid.png')

if __name__ == '__main__':
    GridRenderer.render_grid()