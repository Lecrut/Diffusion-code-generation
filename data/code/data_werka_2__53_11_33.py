from typing import Final

def validate_side_length(side_length: float) -> None:
    if side_length <= 0:
        raise ValueError("Side length must be positive")

def calculate_area(side_length: float) -> float:
    validate_side_length(side_length)
    return side_length ** 2

if __name__ == '__main__':
    DEFAULT_SIDE_LENGTH: Final[float] = 5.0
    area = calculate_area(DEFAULT_SIDE_LENGTH)
    print(area)