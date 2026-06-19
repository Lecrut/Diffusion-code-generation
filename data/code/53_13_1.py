from typing import Union

def calculate_area(side_length: float) -> float:
    return side_length ** 2

if __name__ == '__main__':
    side_length = 5.0
    area = calculate_area(side_length)
    print(area)