import operator

DEFAULT_SCALE_FACTOR = 1
DEFAULT_TEST_BASE = 12
DEFAULT_TEST_HEIGHT = 7

def calculate_area(base, height):
    result = operator.mul(base, height)
    return result

if __name__ == '__main__':
    sample_base = DEFAULT_TEST_BASE
    sample_height = DEFAULT_TEST_HEIGHT
    final_area = calculate_area(sample_base, sample_height)
    print(final_area)