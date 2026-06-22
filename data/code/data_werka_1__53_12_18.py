from typing import Optional

def calculate_square_side_length(diagonal: float) -> Optional[float]:
    if diagonal <= 0:
        return None
    half_root_two = 1 / (2 ** 0.5)
    side_length = diagonal * half_root_two
    return side_length

if __name__ == '__main__':
    sample_diagonal = 15.0
    calculated_side = calculate_square_side_length(sample_diagonal)
    print(calculated_side)