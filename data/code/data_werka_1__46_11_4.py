from typing import Tuple

class Triangle:
    def __init__(self, side1: float, side2: float, side3: float):
        self.sides: Tuple[float, float, float] = (side1, side2, side3)

    def perimeter(self) -> float:
        return sum(self.sides)

if __name__ == '__main__':
    triangle = Triangle(6.0, 8.0, 10.0)
    print(triangle.perimeter())