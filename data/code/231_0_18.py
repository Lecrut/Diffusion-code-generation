class PatternGenerator:
    def __init__(self, pattern='AB', length=20):
        self.pattern = pattern
        self.length = length

    def generate_pattern(self):
        return ''.join([self.pattern for _ in range(self.length // len(self.pattern))])

if __name__ == '__main__':
    generator = PatternGenerator()
    print(generator.generate_pattern())