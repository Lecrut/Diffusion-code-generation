from typing import List

class Triangle:
    def __init__(self, side1: float, side2: float, side3: float):
        self.sides: List[float] = [side1, side2, side3]

    def perimeter(self) -> float:
        return sum(self.sides)

if __name__ == '__main__':
    triangle = Triangle(3.0, 4.0, 5.0)
    print(triangle.perimeter())