class TrianglePatternGenerator:
    def __init__(self, height):
        self.height = height

    def generate_pattern(self):
        return '\n'.join(['*' * (i + 1) for i in range(self.height)])

if __name__ == '__main__':
    generator = TrianglePatternGenerator(5)
    print(generator.generate_pattern())