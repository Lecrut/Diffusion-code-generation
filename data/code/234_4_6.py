class CheckerboardGenerator:
    EMPTY = 0
    FILLED = 1

    @staticmethod
    def generate_checkerboard(n):
        return [[(i + j) % 2 for j in range(n)] for i in range(n)]

if __name__ == '__main__':
    generator = CheckerboardGenerator()
    print(generator.generate_checkerboard(4))