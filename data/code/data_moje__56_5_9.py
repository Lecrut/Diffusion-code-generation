class MultiplicationGridGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.grid = None

    def generate(self):
        self.grid = [[row * col for col in range(self.start, self.end + 1)] for row in range(self.start, self.end + 1)]
        return self.grid

    def get_row(self, index):
        return self.grid[index] if self.grid else None

    def get_column(self, index):
        if self.grid is None:
            return None
        return [row[index] for row in self.grid]

    def get_size(self):
        return len(self.grid) if self.grid else 0

if __name__ == '__main__':
    generator = MultiplicationGridGenerator(1, 10)
    result = generator.generate()
    print(result)
    print(generator.get_row(0))
    print(generator.get_column(9))
    print(generator.get_size())