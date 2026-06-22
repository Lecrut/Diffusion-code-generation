class PatternGenerator:
    def __init__(self):
        self.digits = '0123456789'

    def generate_pattern(self, width, height):
        pattern = ""
        for y in range(height):
            for x in range(width):
                digit_index = (x + y) % len(self.digits)
                pattern += self.digits[digit_index]
            pattern += "\n"
        return pattern

if __name__ == '__main__':
    generator = PatternGenerator()
    print(generator.generate_pattern(5, 3))