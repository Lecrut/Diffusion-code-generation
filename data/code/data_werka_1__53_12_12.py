from typing import Final

DIAGONAL_LENGTH: Final[float] = 10.0

def calculate_side_length(diagonal: float) -> float:
    return diagonal / (2 ** 0.5)

if __name__ == '__main__':
    side_length = calculate_side_length(DIAGONAL_LENGTH)
    print(side_length)