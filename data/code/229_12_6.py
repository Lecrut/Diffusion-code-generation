from PIL import Image, ImageDraw

class GridDrawer:
    def __init__(self, size):
        self.size = size
        self.cell_size = 20
        self.image = Image.new('RGB', (size * self.cell_size, size * self.cell_size), 'white')
        self.draw = ImageDraw.Draw(self.image)

    def draw_grid(self):
        for i in range(self.size + 1):
            self.draw.line([(i * self.cell_size, 0), (i * self.cell_size, self.size * self.cell_size)], fill='black')
            self.draw.line([(0, i * self.cell_size), (self.size * self.cell_size, i * self.cell_size)], fill='black')

    def save_grid(self, filename):
        self.image.save(filename)

if __name__ == '__main__':
    grid_drawer = GridDrawer(20)
    grid_drawer.draw_grid()
    grid_drawer.save_grid('grid.png')