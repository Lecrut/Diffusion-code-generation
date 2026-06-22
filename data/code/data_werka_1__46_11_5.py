from typing import Final

class Triangle:
    def __init__(self, side1: float, side2: float, side3: float):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self) -> float:
        return self._sum_sides()

    @staticmethod
    def _sum_sides(side1: float, side2: float, side3: float) -> float:
        return side1 + side2 + side3

if __name__ == '__main__':
    triangle = Triangle(6.0, 8.0, 10.0)
    print(triangle.perimeter())