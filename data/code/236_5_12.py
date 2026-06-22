import numpy as np

class PatternGenerator:
    BASE_PATTERN = np.array([['#', '#'], ['#', ' ']])

    @staticmethod
    def repeat_pattern(base, times):
        return np.tile(base, (times, times))

if __name__ == '__main__':
    repeated_pattern = PatternGenerator.repeat_pattern(PatternGenerator.BASE_PATTERN, 3)
    print(repeated_pattern)