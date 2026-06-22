class PyramidPattern:
    def __init__(self, height):
        self.height = height

    def generate_pattern(self):
        lines = []
        for i in range(1, self.height + 1):
            lines.append(' ' * (self.height - i) + '*' * (2 * i - 1))
        return '\n'.join(lines)

if __name__ == '__main__':
    pyramid = PyramidPattern(5)
    pattern = pyramid.generate_pattern()
    print(pattern)