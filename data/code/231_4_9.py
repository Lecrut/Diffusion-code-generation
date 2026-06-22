class PatternGenerator:
    def __init__(self, length):
        self.length = length

    def generate_pattern(self):
        return [i % 2 for i in range(self.length)]

if __name__ == '__main__':
    generator = PatternGenerator(50)
    pattern = generator.generate_pattern()
    print(pattern)