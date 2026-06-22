from typing import Tuple

class Triangle:
    def __init__(self, sides: Tuple[float, float, float]):
        self.sides = sides

    def perimeter(self) -> float:
        return sum(self.sides)

if __name__ == '__main__':
    triangle_sides = (7.0, 24.0, 25.0)
    triangle = Triangle(triangle_sides)
    print(triangle.perimeter())