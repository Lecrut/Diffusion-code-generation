from typing import Union

class Triangle:
    def __init__(self, side1: float, side2: float, side3: float):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("Side lengths must be positive")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self) -> float:
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    try:
        triangle = Triangle(3.0, 4.0, 5.0)
        print(triangle.perimeter())
    except ValueError as e:
        print(e)