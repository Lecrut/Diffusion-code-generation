from typing import List

class Triangle:
    def __init__(self, sides: List[float]):
        if len(sides) != 3:
            raise ValueError("A triangle must have exactly three sides.")
        self._sides = sides
        self._validate_sides()

    def _validate_sides(self) -> None:
        a, b, c = self._sides
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("All sides must be positive numbers.")
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError("The sum of any two sides must be greater than the third side.")

    def perimeter(self) -> float:
        return sum(self._sides)

if __name__ == '__main__':
    sample_sides1: List[float] = [3.0, 4.0, 5.0]
    triangle1 = Triangle(sample_sides1)
    print(triangle1.perimeter())

    sample_sides2: List[float] = [7.0, 10.0, 5.0]
    try:
        triangle2 = Triangle(sample_sides2)
        print(triangle2.perimeter())
    except ValueError as e:
        print(f"Error: {e}")