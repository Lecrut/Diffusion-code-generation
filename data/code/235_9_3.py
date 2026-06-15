class PatternGenerator:
    @staticmethod
    def generate_diamond(n):
        for i in range(n):
            print("*" * (2 * i + 1))
            print(" " * i * 2)
            print("*" * (2 * (n - 1 - i) + 1))
if __name__ == '__main__':
    PatternGenerator.generate_diamond(5)