from typing import Final

class Triangle:

    def __init__(self, side1: float, side2: float, side3: float):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self) -> float:
        return self.side1 + self.side2 + self.side3
if __name__ == '__main__':
    a: Final[float] = 6.0
    b: Final[float] = 8.0
    c: Final[float] = 10.0
    triangle = Triangle(a, b, c)
    print(triangle.perimeter())