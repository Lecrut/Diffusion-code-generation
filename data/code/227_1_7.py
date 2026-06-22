class StarPatternGenerator:
    def __init__(self, height):
        self.height = height

    def generate_pattern(self):
        pattern = []
        for i in range(self.height):
            spaces = " " * (self.height - 1 - i)
            stars = "*" * (2 * self.height - 1 - 2 * i)
            pattern.append(spaces + stars)
        return pattern

if __name__ == '__main__':
    generator = StarPatternGenerator(4)
    print("\n--- Pattern for n=4 ---")
    print("\n".join(generator.generate_pattern()))