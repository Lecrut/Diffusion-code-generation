from typing import Final

def calculate_area(side_length: float) -> float:
    return side_length ** 2

if __name__ == '__main__':
    SIDE_LENGTH: Final[float] = 5.0
    area = calculate_area(SIDE_LENGTH)
    print(area)