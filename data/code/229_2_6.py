from PIL import Image

class GridRenderer:
    def __init__(self, size=256):
        self.size = size
        self.cell_size = size // 8
        self.image = Image.new('RGB', (size, size), 'white')
    
    @staticmethod
    def fill_cell(draw, x, y, color):
        for i in range(x, x + 16):
            for j in range(y, y + 16):
                draw.point((i, j), fill=color)
    
    def render_grid(self):
        draw = self.image.load()
        for i in range(0, self.size, self.cell_size * 2):
            for j in range(0, self.size, self.cell_size * 2):
                color = 'black' if (i + j) % (self.cell_size * 4) == 0 else 'white'
                self.fill_cell(draw, i, j, color)
    
    def save_grid(self):
        self.image.save('grid_pattern.png')

if __name__ == '__main__':
    renderer = GridRenderer()
    renderer.render_grid()
    renderer.save_grid()