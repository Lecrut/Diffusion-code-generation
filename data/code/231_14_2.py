class PatternGenerator:
    def generate_square(self, size):
        for i in range(size):
            line = "*" * (2 * i + 1)
            print(line)
if __name__ == '__main__':
    generator = PatternGenerator()
    size = 5
    print(f"Generating square pattern of size {size}:")
    generator.generate_square(size)