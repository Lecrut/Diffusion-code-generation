from typing import Sequence

class Triangle:
    def __init__(self, sides: Sequence[float]):
        self.sides = tuple(sides)

    def perimeter(self) -> float:
        return sum(self.sides)

if __name__ == '__main__':
    SIDES = (5.0, 12.0, 13.0)
    triangle = Triangle(SIDES)
    print(triangle.perimeter())