class PatternGenerator:
    def generate_square(self, size):
        for i in range(size):
            print("=" * (2 * i + 1))
            print("#" * (2 * i + 1))
if __name__ == '__main__':
    generator = PatternGenerator()
    size = 5
    generator.generate_square(size)