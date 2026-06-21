class Triangle:
    def __init__(self, side1, side2, side3):
        self._validate_sides(side1, side2, side3)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def _validate_sides(self, side1, side2, side3):
        if not all(isinstance(x, (int, float)) for x in [side1, side2, side3]):
            raise ValueError("All sides must be numbers.")
        if not all(x > 0 for x in [side1, side2, side3]):
            raise ValueError("All sides must be positive numbers.")
        if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
            raise ValueError("The given sides do not form a valid triangle.")

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    try:
        triangle = Triangle(10, 6, 8)
        print(f"Perimeter: {triangle.perimeter()}")
        print(f"Sides: Side 1 = {triangle.side1}, Side 2 = {triangle.side2}, Side 3 = {triangle.side3}")
    except ValueError as e:
        print(e)