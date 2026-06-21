from typing import Final
DEFAULT_SIDE_LENGTH: Final[float] = 5.0

def calculate_area(side_length: float) -> float:
    return side_length ** 2
if __name__ == '__main__':
    area = calculate_area(DEFAULT_SIDE_LENGTH)
    print(area)