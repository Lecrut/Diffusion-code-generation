class GridGenerator:
    def __init__(self, size=5):
        self.size = size

    def generate_grid(self):
        return [[(i, j) for j in range(self.size)] for i in range(self.size)]

if __name__ == '__main__':
    generator = GridGenerator()
    grid = generator.generate_grid()
    print(grid)