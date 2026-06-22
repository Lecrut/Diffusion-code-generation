class DiamondPattern:
    ROWS = 5

    @staticmethod
    def draw_diamond():
        for i in range(2 * DiamondPattern.ROWS - 1):
            spaces = abs(DiamondPattern.ROWS - i - 1)
            bars = 2 * min(i, DiamondPattern.ROWS - i) + 1
            print(' ' * spaces + '|' * bars)

if __name__ == '__main__':
    DiamondPattern.draw_diamond()