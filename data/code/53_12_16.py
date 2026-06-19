from math import sqrt

def calculate_square_side(diagonal_length: float) -> float:
    return diagonal_length / sqrt(2)

if __name__ == '__main__':
    diagonal_length = 10.0
    side_length = calculate_square_side(diagonal_length)
    print(side_length)