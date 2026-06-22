class CheckerboardGenerator:
    def __init__(self, size):
        self.size = size

    def generate_pattern(self):
        pattern = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if (i + j) % 2 == 0:
                    row.append('X')
                else:
                    row.append('.')
            pattern.append(''.join(row))
        return '\n'.join(pattern)

if __name__ == '__main__':
    generator = CheckerboardGenerator(4)
    print(generator.generate_pattern())