import math

def calculate_side_length(diagonal: float) -> float:
    if diagonal <= 0:
        raise ValueError('Diagonal length must be positive.')
    half_diagonal = diagonal / 2.0
    side_length = math.sqrt(2 * (half_diagonal ** 2))
    return side_length

if __name__ == '__main__':
    sample_diagonal_length = 15.0
    try:
        calculated_side_length = calculate_side_length(sample_diagonal_length)
        print(f'The side length of the square with diagonal {sample_diagonal_length} is: {calculated_side_length}')
    except ValueError as e:
        print(e)