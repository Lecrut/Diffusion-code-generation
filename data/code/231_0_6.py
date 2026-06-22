class PatternGenerator:
    def generate_pattern(self, pattern, length):
        return ''.join([pattern for _ in range(length // len(pattern))])

if __name__ == '__main__':
    generator = PatternGenerator()
    sample_pattern = 'AB'
    sample_length = 20
    result = generator.generate_pattern(sample_pattern, sample_length)
    print(result)