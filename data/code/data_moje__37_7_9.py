import operator

PARALLELOGRAM_BASE = 7
PARALLELOGRAM_HEIGHT = 9

def calculate_area(base, height):
    product = operator.mul(base, height)
    return product

if __name__ == '__main__':
    sample_base = PARALLELOGRAM_BASE
    sample_height = PARALLELOGRAM_HEIGHT
    computed_area = calculate_area(sample_base, sample_height)
    print(computed_area)