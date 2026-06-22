import numpy as np

class PatternTiler:
    BASE_PATTERN = np.array([['#', '#'], ['#', ' '], ['#', '#']])

    @staticmethod
    def repeat_pattern(base, rows, cols):
        return np.tile(base, (rows, cols))

if __name__ == '__main__':
    tiler = PatternTiler()
    repeated_pattern = tiler.repeat_pattern(PatternTiler.BASE_PATTERN, 3, 2)
    print(repeated_pattern)