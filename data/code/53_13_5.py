from typing import Union

def validate_side_length(side_length: float) -> None:
    if side_length <= 0:
        raise ValueError("Side length must be positive")

def calculate_area(side_length: float) -> float:
    validate_side_length(side_length)
    return side_length ** 2

if __name__ == '__main__':
    side_length = 5.0
    area = calculate_area(side_length)
    print(area)