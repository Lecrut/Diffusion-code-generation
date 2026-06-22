class MultiplicationTableGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def build_grid(self):
        return [[row * col for col in range(self.start, self.end + 1)] for row in range(self.start, self.end + 1)]

    def get_row(self, index):
        return self.build_grid()[index]

    def get_value(self, row, col):
        return (row + 1) * (col + 1)

if __name__ == '__main__':
    generator = MultiplicationTableGenerator(1, 10)
    full_grid = generator.build_grid()
    specific_row = generator.get_row(4)
    specific_val = generator.get_value(5, 6)
    print(full_grid)
    print(specific_row)
    print(specific_val)