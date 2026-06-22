import numpy as np

class PatternGenerator:
    DEFAULT_PATTERN = [True, False]

    @staticmethod
    def generate_pattern(n):
        return list(np.tile(PatternGenerator.DEFAULT_PATTERN, (n // 2) + 1))[:n]

if __name__ == '__main__':
    sample_pattern = PatternGenerator.generate_pattern(25)
    print(sample_pattern)