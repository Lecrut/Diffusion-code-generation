from typing import Tuple

class Triangle:
    def __init__(self, side1: float, side2: float, side3: float):
        self.sides = (side1, side2, side3)

    def perimeter(self) -> float:
        return sum(self.sides)

if __name__ == '__main__':
    DEFAULT_SIDES: Tuple[float, float, float] = (7.0, 9.0, 12.0)
    triangle = Triangle(*DEFAULT_SIDES)
    print(triangle.perimeter())