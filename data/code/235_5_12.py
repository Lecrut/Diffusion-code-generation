class TrianglePattern:
    MAX_VALUE = 5

    @staticmethod
    def generate_pattern():
        pattern = []
        for i in range(1, TrianglePattern.MAX_VALUE + 1):
            spaces = ' ' * (TrianglePattern.MAX_VALUE - i)
            numbers = ''.join(str(j) for j in range(1, i + 1))
            pattern.append(spaces + numbers)
        return '\n'.join(pattern)

if __name__ == '__main__':
    triangle = TrianglePattern()
    print(triangle.generate_pattern())