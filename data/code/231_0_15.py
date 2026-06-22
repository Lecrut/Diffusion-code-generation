class PatternGenerator:
    def generate_pattern(self, length):
        return ''.join(['AB' for _ in range(length // 2)])

if __name__ == '__main__':
    generator = PatternGenerator()
    pattern = generator.generate_pattern(20)
    print(pattern)