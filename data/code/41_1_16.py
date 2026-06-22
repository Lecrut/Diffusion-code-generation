from typing import Union

def compute_rhombus_area(d1: Union[int, float], d2: Union[int, float]) -> float:
    return 0.5 * d1 * d2

if __name__ == '__main__':
    diagonal_one: int = 10
    diagonal_two: int = 8
    result: float = compute_rhombus_area(diagonal_one, diagonal_two)
    print(result)