from typing import NamedTuple

class Triangle(NamedTuple):
    side1: float
    side2: float
    side3: float

    def perimeter(self) -> float:
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    triangle = Triangle(6.0, 8.0, 10.0)
    print(triangle.perimeter())