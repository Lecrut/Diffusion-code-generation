from typing import Union

def compute_rhombus_area(diagonal1: Union[int, float], diagonal2: Union[int, float]) -> float:
    return (diagonal1 * diagonal2) / 2.0

if __name__ == '__main__':
    diag_a: float = 10
    diag_b: float = 8
    area: float = compute_rhombus_area(diag_a, diag_b)
    print(area)