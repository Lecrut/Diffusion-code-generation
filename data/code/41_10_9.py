from typing import Union

def calculate_rhombus_area(diagonal_1: float, diagonal_2: float) -> float:
    return (diagonal_1 * diagonal_2) / 2

if __name__ == '__main__':
    d1 = 10.0
    d2 = 6.5
    area = calculate_rhombus_area(d1, d2)
    print(area)