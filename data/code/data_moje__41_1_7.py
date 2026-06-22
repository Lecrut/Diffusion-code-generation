from typing import Union

def compute_rhombus_area(d1: float, d2: float) -> float:
    return 0.5 * d1 * d2

if __name__ == '__main__':
    diagonal_1: float = 10.0
    diagonal_2: float = 8.0
    area: float = compute_rhombus_area(diagonal_1, diagonal_2)
    print(area)