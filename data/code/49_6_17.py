class StarGridGenerator:
    def __init__(self, size):
        self.size = size

    def generate_row(self, row_index):
        return '*' * self.size

    def process(self, output_func):
        for i in range(self.size):
            line = self.generate_row(i)
            output_func(line)

def create_grid_printer(n):
    generator = StarGridGenerator(n)
    generator.process(print)

if __name__ == '__main__':
    create_grid_printer(10)