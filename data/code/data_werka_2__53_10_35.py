from math import sqrt

def calculate_side_length(diagonal: float) -> float:
    if diagonal <= 0:
        raise ValueError("Diagonal length must be positive.")
    return diagonal / sqrt(2)

if __name__ == '__main__':
    DIAGONAL_LENGTH = 10.0
    try:
        side_length = calculate_side_length(DIAGONAL_LENGTH)
        print(f"The side length of the square with diagonal {DIAGONAL_LENGTH} is: {side_length}")
    except ValueError as e:
        print(e)