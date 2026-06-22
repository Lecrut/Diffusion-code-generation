from math import sqrt
DIAGONAL_LENGTH = 10.0

def calculate_side_length(diagonal: float) -> float:
    CONVERSION_FACTOR = 1 / sqrt(2)
    return diagonal * CONVERSION_FACTOR
if __name__ == '__main__':
    side_length = calculate_side_length(DIAGONAL_LENGTH)
    print(f'The side length of the square with diagonal {DIAGONAL_LENGTH} is: {side_length}')