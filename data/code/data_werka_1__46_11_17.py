from typing import List

class Triangle:
    def __init__(self, side1: float, side2: float, side3: float):
        self.sides: List[float] = [side1, side2, side3]
        if not self._is_valid_triangle():
            raise ValueError("Invalid triangle sides")

    def _is_valid_triangle(self) -> bool:
        a, b, c = sorted(self.sides)
        return a + b > c

    def perimeter(self) -> float:
        return sum(self.sides)

if __name__ == '__main__':
    side_a = 3.0
    side_b = 4.0
    side_c = 5.0
    triangle_instance = Triangle(side_a, side_b, side_c)
    print(triangle_instance.perimeter())