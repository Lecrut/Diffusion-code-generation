from typing import Final

def calculate_area(side_length: float) -> float:
    return side_length * side_length

if __name__ == '__main__':
    DEFAULT_SIDE_LENGTH: Final[float] = 5.0
    computed_side_length = DEFAULT_SIDE_LENGTH
    area = calculate_area(computed_side_length)
    print(area)