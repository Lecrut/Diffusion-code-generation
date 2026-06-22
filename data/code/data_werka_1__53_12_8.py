from typing import Dict

def calculate_square_side_length(diagonal: float) -> float:
    constants: Dict[str, float] = {
        'sqrt_2': 1.4142135623730951
    }
    side_length = diagonal / constants['sqrt_2']
    return side_length

if __name__ == '__main__':
    diagonal_length = 10.0
    side_length = calculate_square_side_length(diagonal_length)
    print(side_length)