class PatternGenerator:
    def generate_square(self, size):
        for i in range(size):
            print("=" * (2 * i + 1))
            for j in range(2 * i + 1):
                if i == 0 or j == 0 or j == (2 * i):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
if __name__ == '__main__':
    generator = PatternGenerator()
    size = 5
    generator.generate_square(size)