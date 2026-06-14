class PatternGenerator:
    def generate_square(self, size):
        for i in range(size):
            line = "*" * (2 * i + 1)
            print(line)
if __name__ == '__main__':
    generator = PatternGenerator()
    size = 5
    generator.generate_square(size)