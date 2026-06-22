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

if __name__ == '__main__':
    triangle = TrianglePattern()
    print(triangle.generate_pattern())