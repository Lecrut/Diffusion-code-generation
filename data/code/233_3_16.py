class RectanglePatternGenerator:
    def __init__(self, width=5, height=3):
        self.width = width
        self.height = height

    def generate_pattern(self):
        pattern = ""
        for y in range(self.height):
            for x in range(self.width):
                digit = (x + y) % 10
                pattern += str(digit)
            pattern += "\n"
        return pattern

if __name__ == '__main__':
    generator = RectanglePatternGenerator(5, 3)
    print(generator.generate_pattern())