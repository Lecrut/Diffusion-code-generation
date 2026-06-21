from typing import Tuple

class Triangle:
    def __init__(self, sides: Tuple[float, float, float]):
        self.sides = sides
        if not self._is_valid_triangle():
            raise ValueError("Invalid triangle sides")

    def perimeter(self) -> float:
        return sum(self.sides)

    def _is_valid_triangle(self) -> bool:
        a, b, c = sorted(self.sides)
        return a + b > c

if __name__ == '__main__':
    try:
        triangle = Triangle((3.0, 4.0, 5.0))
        print(triangle.perimeter())
    except ValueError as e:
        print(e)