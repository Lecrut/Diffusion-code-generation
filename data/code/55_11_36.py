from typing import List

class Triangle:
    MIN_SIDE_LENGTH = 0.1

    @staticmethod
    def validate_sides(sides: List[float]) -> None:
        if len(sides) != 3:
            raise ValueError("A triangle must have exactly three sides.")
        for side in sides:
            if side <= Triangle.MIN_SIDE_LENGTH:
                raise ValueError(f"Sides must be greater than {Triangle.MIN_SIDE_LENGTH}.")
        a, b, c = sides
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError("The sum of any two sides must be greater than the third side.")

    def __init__(self, side_a: float, side_b: float, side_c: float):
        self._sides = [side_a, side_b, side_c]
        Triangle.validate_sides(self._sides)

    def perimeter(self) -> float:
        return sum(self._sides)

if __name__ == '__main__':
    sample_sides = [9.0, 12.0, 15.0]
    try:
        triangle = Triangle(*sample_sides)
        print(triangle.perimeter())
    except ValueError as e:
        print(f"Error: {e}")