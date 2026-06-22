class PatternGenerator:
    def generate_pattern(self, length):
        return [i % 2 for i in range(length)]

if __name__ == '__main__':
    generator = PatternGenerator()
    pattern = generator.generate_pattern(50)
    print(pattern)