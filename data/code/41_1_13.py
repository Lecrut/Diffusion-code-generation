from typing import Union

def rhombus_area(d1: Union[int, float], d2: Union[int, float]) -> float:
    return 0.5 * d1 * d2

if __name__ == '__main__':
    diagonal_1 = 10
    diagonal_2 = 8
    area = rhombus_area(diagonal_1, diagonal_2)
    print(area)