class PatternGenerator:
    def __init__(self, pattern='AB', length=20):
        self.pattern = pattern * ((length // len(pattern)) + 1)
        self.length = length

    def get_pattern(self):
        return ''.join(self.pattern[:self.length])

if __name__ == '__main__':
    generator = PatternGenerator()
    print(generator.get_pattern())