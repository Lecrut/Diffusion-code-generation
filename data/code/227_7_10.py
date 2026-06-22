class StarPattern:
    def __init__(self, rows):
        self.rows = rows

    def print_pattern(self):
        for i in reversed(range(1, self.rows + 1)):
            spaces = " " * (self.rows - i)
            stars = "*" * (2 * i - 1)
            print(spaces + stars)

if __name__ == '__main__':
    pattern = StarPattern(5)
    pattern.print_pattern()