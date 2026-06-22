class DiamondPattern:
    MAX_WIDTH = 5

    @staticmethod
    def generate_diamond():
        middle = DiamondPattern.MAX_WIDTH // 2
        for i in range(DiamondPattern.MAX_WIDTH):
            if i <= middle:
                spaces = middle - i
                stars = 2 * i + 1
            else:
                spaces = i - middle
                stars = 2 * (DiamondPattern.MAX_WIDTH - i) + 1
            yield " " * spaces + "*" * stars

if __name__ == '__main__':
    diamond = DiamondPattern.generate_diamond()
    for row in diamond:
        print(row)