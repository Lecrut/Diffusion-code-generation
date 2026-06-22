class RectanglePatternGenerator:
    def __init__(self):
        self.digits = '0123456789'

    def generate_pattern(self, width, height):
        pattern = '\n'.join(self._row(width) for _ in range(height))
        return pattern

    def _row(self, width):
        return ''.join(self.digits[i % len(self.digits)] for i in range(width))

if __name__ == '__main__':
    generator = RectanglePatternGenerator()
    print(generator.generate_pattern(5, 3))