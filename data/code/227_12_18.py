class DiamondStarPattern:
    def __init__(self, max_width):
        self.max_width = max_width

    def generate_pattern(self):
        half = self.max_width // 2 + 1
        upper_half = [('*' * (2 * i + 1)).center(self.max_width) for i in range(half)]
        lower_half = upper_half[-2::-1]
        return upper_half + lower_half

    def print_pattern(self):
        for line in self.generate_pattern():
            print(line)

if __name__ == '__main__':
    diamond = DiamondStarPattern(7)
    diamond.print_pattern()