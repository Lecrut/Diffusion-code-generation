class DiamondPattern:
    def __init__(self, max_width):
        self.max_width = max_width

    def generate_line(self, i):
        spaces = abs(i - (self.max_width // 2))
        stars = 1 + 4 * min(spaces, self.max_width - spaces)
        return " " * spaces + "*" * stars

    def print_diamond(self):
        for i in range(self.max_width):
            print(self.generate_line(i))

if __name__ == '__main__':
    diamond = DiamondPattern(5)
    diamond.print_diamond()