class ZigzagGenerator:
    def __init__(self, width):
        self.width = width

    def generate_line(self, line_number):
        if line_number % 2 == 0:
            return '*' * (line_number + 1)
        else:
            spaces = ' ' * (self.width - line_number - 1)
            stars = '*' * (line_number + 1)
            return spaces + stars

    def generate_pattern(self, height):
        pattern = []
        for y in range(height):
            line = self.generate_line(y)
            if y % 2 == 1:
                line = line[::-1]
            pattern.extend(line.split('\n'))
        return '\n'.join(pattern)

if __name__ == '__main__':
    generator = ZigzagGenerator(5)
    print(generator.generate_pattern(3))