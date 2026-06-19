from typing import Union

def calculate_square_side(diagonal: float) -> float:
    return diagonal / (2 ** 0.5)

if __name__ == '__main__':
    diagonal_length = 10.0
    side_length = calculate_square_side(diagonal_length)
    print(side_length)