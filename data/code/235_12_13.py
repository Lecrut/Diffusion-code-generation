class PyramidPatternGenerator:
    def __init__(self):
        self.pattern = []

    @staticmethod
    def generate_line(n, max_width):
        return ' ' * (max_width - n) + '*' * (2 * n - 1)

    def add_line(self, n, max_width):
        line = self.generate_line(n, max_width)
        self.pattern.append(line)

    def print_pattern(self, n):
        max_width = n * 2 - 1
        for i in range(1, n + 1):
            self.add_line(i, max_width)
        return '\n'.join(self.pattern)

if __name__ == '__main__':
    generator = PyramidPatternGenerator()
    sample_number = 5
    pattern = generator.print_pattern(sample_number)
    print(pattern)