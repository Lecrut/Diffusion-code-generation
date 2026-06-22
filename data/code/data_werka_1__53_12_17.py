from typing import Final
DIAGONAL_LENGTH: Final[float] = 10.0

def calculate_square_side_length(diagonal: float) -> float:
    CONVERSION_FACTOR: Final[float] = 2 ** 0.5
    return diagonal / CONVERSION_FACTOR
if __name__ == '__main__':
    side_length = calculate_square_side_length(DIAGONAL_LENGTH)
    print(side_length)