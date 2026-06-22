from typing import Final

DIAGONAL_LENGTH: Final[float] = 10.0

def calculate_square_side_length(diagonal: float) -> float:
    if diagonal <= 0:
        raise ValueError("Diagonal length must be positive")
    return diagonal / (2 ** 0.5)

if __name__ == '__main__':
    side_length = calculate_square_side_length(DIAGONAL_LENGTH)
    print(side_length)