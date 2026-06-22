from typing import Optional

def calculate_square_side_length(diagonal: float) -> float:
    if diagonal <= 0:
        raise ValueError('Diagonal length must be positive.')
    import math
    side_length = diagonal / math.sqrt(2)
    return side_length
if __name__ == '__main__':
    hard_coded_diagonal = 10.0
    side_length = calculate_square_side_length(hard_coded_diagonal)
    print(side_length)