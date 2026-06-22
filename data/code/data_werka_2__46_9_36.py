from typing import Tuple

def validate_sides(sides: Tuple[float, float, float]) -> None:
    if len(sides) != 3:
        raise ValueError("Exactly three sides are required.")
    for side in sides:
        if side <= 0:
            raise ValueError("All sides must be positive numbers.")

class Triangle:
    def __init__(self, side1: float, side2: float, side3: float):
        validate_sides((side1, side2, side3))
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self) -> float:
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    try:
        triangle = Triangle(7.0, 9.0, 12.0)
        print(triangle.perimeter())
    except ValueError as e:
        print(e)