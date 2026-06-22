class HollowRectanglePattern:
    def __init__(self, width=6, height=4):
        self.WIDTH = width
        self.HEIGHT = height

    @staticmethod
    def generate_line(width, is_first_or_last):
        if is_first_or_last:
            return "*" * width
        else:
            return "*" + " " * (width - 2) + "*"

    def generate_pattern(self):
        pattern = []
        for i in range(self.HEIGHT):
            is_first_or_last = i == 0 or i == self.HEIGHT - 1
            line = self.generate_line(self.WIDTH, is_first_or_last)
            pattern.append(line)
        return pattern

if __name__ == '__main__':
    pattern_generator = HollowRectanglePattern()
    pattern = pattern_generator.generate_pattern()
    for line in pattern:
        print(line)