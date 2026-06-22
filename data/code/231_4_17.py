class PatternGenerator:
    PATTERN = [0, 1]

    @staticmethod
    def generate_pattern(length):
        return [PatternGenerator.PATTERN[i % len(PatternGenerator.PATTERN)] for i in range(length)]

if __name__ == '__main__':
    sample_length = 50
    pattern = PatternGenerator.generate_pattern(sample_length)
    print(pattern)