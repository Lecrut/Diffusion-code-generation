from PIL import Image, ImageDraw

class GridCreator:
    def __init__(self, size):
        self.size = size
        self.cell_size = 20
        self.image = Image.new('RGB', (size * self.cell_size, size * self.cell_size), 'white')
        self.draw = ImageDraw.Draw(self.image)

    def draw_grid(self):
        for i in range(self.size + 1):
            self.draw.line([(i * self.cell_size, 0), (i * self.cell_size, self.size * self.cell_size)], fill='black')
            self.draw.line([(0, i * self.cell_size), (self.size * self.cell_size, i * self.cell_size)], fill='black')

    def save_image(self):
        self.image.save('grid.png')

if __name__ == '__main__':
    grid_creator = GridCreator(20)
    grid_creator.draw_grid()
    grid_creator.save_image()