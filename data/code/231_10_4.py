class PatternGenerator:
    PATTERN = ['A', 'B', 'C']

    @staticmethod
    def generate_pattern(n):
        return [PatternGenerator.PATTERN[i % 3] for i in range(n)]

if __name__ == '__main__':
    sample_output = PatternGenerator.generate_pattern(15)
    print(sample_output)