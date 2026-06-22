class PatternGenerator:
    def __init__(self):
        self.pattern = 'abcde'

    def generate_pattern(self, length):
        return (self.pattern * ((length // len(self.pattern)) + 1))[:length]

if __name__ == '__main__':
    generator = PatternGenerator()
    result = generator.generate_pattern(50)
    print(result)