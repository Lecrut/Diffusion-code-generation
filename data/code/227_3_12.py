class DiamondPattern:
    def __init__(self, max_width):
        self.max_width = max_width

    def generate_diamond(self):
        middle = self.max_width // 2
        for i in range(self.max_width):
            if i <= middle:
                spaces = middle - i
                stars = 2 * i + 1
            else:
                spaces = i - middle
                stars = 2 * (self.max_width - i) + 1
            yield " " * spaces + "*" * stars

if __name__ == '__main__':
    diamond = DiamondPattern(5)
    for row in diamond.generate_diamond():
        print(row)