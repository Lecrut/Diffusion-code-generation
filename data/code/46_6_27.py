class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.sides = [side_a, side_b, side_c]
        self._validate_sides()

    def _validate_sides(self):
        if any(side <= 0 for side in self.sides):
            raise ValueError("All sides must be positive numbers.")
        a, b, c = sorted(self.sides)
        if not (a + b > c):
            raise ValueError("The given sides do not form a valid triangle.")

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    try:
        triangle = Triangle(10, 6, 8)
        print(f"Perimeter: {triangle.perimeter()}")
        print(f"Sides: {triangle.sides}")
    except ValueError as e:
        print(e)