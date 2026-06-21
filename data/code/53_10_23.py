from typing import Optional

def calculate_square_side(diagonal: float) -> float:
    if diagonal <= 0:
        raise ValueError('Diagonal length must be positive.')
    side_length = diagonal / 2 ** 0.5
    return side_length
if __name__ == '__main__':
    diagonal_length = 10.0
    try:
        side_length = calculate_square_side(diagonal_length)
        print(f'The side length of the square with diagonal {diagonal_length} is: {side_length}')
    except ValueError as e:
        print(e)