from typing import NamedTuple

class SideLengths(NamedTuple):
    side1: float
    side2: float
    side3: float

class Triangle:

    def __init__(self, sides: SideLengths):
        self.sides = sides

    def perimeter(self) -> float:
        return sum(self.sides)
if __name__ == '__main__':
    triangle_sides = SideLengths(6.0, 8.0, 10.0)
    triangle_instance = Triangle(triangle_sides)
    print('Perimeter:', triangle_instance.perimeter())
    another_triangle_sides = SideLengths(3.0, 4.0, 5.0)
    another_triangle_instance = Triangle(another_triangle_sides)
    print('Another Perimeter:', another_triangle_instance.perimeter())