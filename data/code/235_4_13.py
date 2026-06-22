class RectanglePattern:
    WIDTH = 6
    HEIGHT = 4

    @staticmethod
    def generate_pattern():
        pattern = []
        for i in range(RectanglePattern.HEIGHT):
            if i == 0 or i == RectanglePattern.HEIGHT - 1:
                line = "*" * RectanglePattern.WIDTH
            else:
                line = "*" + " " * (RectanglePattern.WIDTH - 2) + "*"
            pattern.append(line)
        return pattern

if __name__ == '__main__':
    pattern = RectanglePattern.generate_pattern()
    for line in pattern:
        print(line)