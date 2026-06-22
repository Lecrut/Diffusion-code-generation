from math import sqrt

def calculate_side_length(diagonal: float) -> float:
    if diagonal <= 0:
        raise ValueError('Diagonal length must be positive.')
    root_two = sqrt(2)
    side_length = diagonal / root_two
    return side_length
if __name__ == '__main__':
    diagonal_length = 15.0
    try:
        side_length = calculate_side_length(diagonal_length)
        print(f'The side length of the square with diagonal {diagonal_length} is: {side_length}')
    except ValueError as e:
        print(e)