class IsoscelesTriangleGenerator:
    def __init__(self, height):
        self.height = height
        self.pattern_lines = []
        self._build_pattern()

    def _build_pattern(self):
        for i in range(1, self.height + 1):
            num_stars = 2 * i - 1
            num_spaces = self.height - i
            self.pattern_lines.append(' ' * num_spaces + '*' * num_stars)

    def get_pattern(self):
        return '\n'.join(self.pattern_lines)

    def get_row_count(self):
        return len(self.pattern_lines)

    def get_max_width(self):
        if not self.pattern_lines:
            return 0
        return len(self.pattern_lines[-1])

if __name__ == '__main__':
    generator = IsoscelesTriangleGenerator(7)
    print(generator.get_pattern())
    print(generator.get_row_count())
    print(generator.get_max_width())