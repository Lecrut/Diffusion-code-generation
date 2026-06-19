from typing import Tuple

class Triangle:
    def __init__(self, sides: Tuple[float, float, float]):
        self.sides = sides

    @staticmethod
    def validate_sides(sides: Tuple[float, float, float]) -> bool:
        a, b, c = sides
        return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

    @property
    def perimeter(self) -> float:
        if not self.validate_sides(self.sides):
            raise ValueError("Invalid triangle sides")
        return sum(self.sides)

if __name__ == '__main__':
    sample_sides = (3.0, 4.0, 5.0)
    t = Triangle(sample_sides)
    print(t.perimeter)