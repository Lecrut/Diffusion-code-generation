class ZigzagPattern:
    def __init__(self, width):
        self.width = width

    def generate_line(self, row):
        if row % 2 == 0:
            return '*' * (row + 1)
        else:
            return ' ' * (self.width - row - 1) + '*' * (row + 1)

    def print_pattern(self):
        for i in range(self.width):
            print(self.generate_line(i))

if __name__ == '__main__':
    pattern = ZigzagPattern(5)
    pattern.print_pattern()