class PatternGenerator:
    @staticmethod
    def generate_diamond(N):
        for i in range(N):
            spaces = N - 1 - i
            stars = 2 * i + 1
            line = " " * spaces + "*" * stars
            print(line)
            print(" " * spaces + "*" * (2 * (N - 1 - i) + 1))
if __name__ == '__main__':
    PatternGenerator.generate_diamond(5)