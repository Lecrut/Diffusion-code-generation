from math import sqrt

def validate_diagonal(diagonal: float) -> None:
    if diagonal <= 0:
        raise ValueError('Diagonal length must be positive.')

def calculate_side_length(diagonal: float) -> float:
    validate_diagonal(diagonal)
    return diagonal / sqrt(2)

if __name__ == '__main__':
    diagonal_length = 10.0
    try:
        side_length = calculate_side_length(diagonal_length)
        print(side_length)
    except ValueError as e:
        print(e)