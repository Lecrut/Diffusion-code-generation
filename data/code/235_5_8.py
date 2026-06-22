class TrianglePattern:
    def __init__(self, max_value=5):
        self.max_value = max_value

    def generate_pattern(self):
        pattern = []
        for i in range(1, self.max_value + 1):
            spaces = ' ' * (self.max_value - i)
            numbers = ''.join(str(j) for j in range(1, i + 1))
            pattern.append(spaces + numbers)
        return '\n'.join(pattern)

    def print_pattern(self):
        print(self.generate_pattern())

if __name__ == '__main__':
    triangle = TrianglePattern()
    triangle.print_pattern()