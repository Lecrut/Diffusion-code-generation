class StarPattern:
    def __init__(self, rows):
        self.rows = rows

    def generate_pattern(self):
        pattern = []
        for i in range(self.rows, 0, -1):
            line = " " * (self.rows - i) + "*" * (2 * i - 1)
            pattern.append(line)
        return pattern

if __name__ == '__main__':
    star_pattern_instance = StarPattern(6)
    pattern = star_pattern_instance.generate_pattern()
    for line in pattern:
        print(line)