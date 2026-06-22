from dataclasses import dataclass
from typing import Tuple

DIAGONAL_AREA_MULTIPLIER = 0.5
DIAGONAL_AREA_DIVISOR = 2.0

@dataclass
class RhombusGeometry:
    diagonal_one: float
    diagonal_two: float

    def calculate_area(self) -> float:
        return self.diagonal_one * self.diagonal_two * DIAGONAL_AREA_MULTIPLIER

def compute_rhombus_area(d1: float, d2: float) -> float:
    return d1 * d2 / DIAGONAL_AREA_DIVISOR

if __name__ == '__main__':
    geom = RhombusGeometry(12.0, 8.0)
    area_from_class = geom.calculate_area()
    area_from_func = compute_rhombus_area(12.0, 8.0)
    print(area_from_class)
    print(area_from_func)