class PatternGenerator:
    def generate_diagonal_pattern(self, size):
        for i in range(size):
            for j in range(size):
                if i == j:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
if __name__ == '__main__':
    generator = PatternGenerator()
    size = 5
    generator.generate_diagonal_pattern(size)