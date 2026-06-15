class PatternGenerator:
    @staticmethod
    def generate_diamond(n):
        for i in range(1, n + 1):
            print("*" * (2 * i - 1))
            if i < n:
                print(" " * (n - i) + "*" * (2 * i - 1))
if __name__ == '__main__':
    PatternGenerator.generate_diamond(5)