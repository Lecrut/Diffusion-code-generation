class RectanglePattern:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def generate(self):
        digits = '0123456789'
        pattern = '\n'.join(digits[i % len(digits)] * self.width for i in range(self.height))
        return pattern

if __name__ == '__main__':
    rect = RectanglePattern(5, 3)
    print(rect.generate())