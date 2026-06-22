class TrianglePattern:
    MAX_VALUE = 5

    @staticmethod
    def generate_pattern(max_value=MAX_VALUE):
        pattern = []
        for i in range(1, max_value + 1):
            spaces = ' ' * (max_value - i)
            numbers = ''.join(str(j) for j in range(1, i + 1))
            pattern.append(spaces + numbers)
        return '\n'.join(pattern)

if __name__ == '__main__':
    triangle = TrianglePattern()
    print(triangle.generate_pattern())