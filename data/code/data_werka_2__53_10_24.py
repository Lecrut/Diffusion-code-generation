from typing import Optional

def calculate_square_side_length(diagonal: float) -> float:
    if diagonal <= 0:
        raise ValueError('Diagonal length must be positive')
    side_length = diagonal / 2 ** 0.5
    return side_length
if __name__ == '__main__':
    diagonal_length = 10.0
    side_length = calculate_square_side_length(diagonal_length)
    print(side_length)