class RectangleGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def generate_grid(self, symbol):
        return [symbol * self.width for _ in range(self.height)]

if __name__ == '__main__':
    grid = RectangleGrid(5, 3)
    print(grid.generate_grid('#'))