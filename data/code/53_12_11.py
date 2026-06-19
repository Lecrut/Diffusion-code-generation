from typing import Optional

def validate_diagonal(diagonal: float) -> bool:
    return diagonal > 0

def calculate_side_length(diagonal: float) -> Optional[float]:
    if not validate_diagonal(diagonal):
        return None
    side_length = diagonal * (2 ** -0.5)
    return side_length

if __name__ == '__main__':
    diagonal_length = 10.0
    side_length = calculate_side_length(diagonal_length)
    print(side_length)