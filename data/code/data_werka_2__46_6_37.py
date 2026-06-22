class Triangle:
    def __init__(self, side1, side2, side3):
        self._validate_sides(side1, side2, side3)
        self.sides = [side1, side2, side3]

    def _validate_sides(self, side1, side2, side3):
        if not all(isinstance(x, (int, float)) and x > 0 for x in (side1, side2, side3)):
            raise ValueError("All sides must be positive numbers.")
        if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
            raise ValueError("The given sides do not form a valid triangle.")

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    try:
        triangle = Triangle(6, 8, 10)
        print(triangle.perimeter())
    except ValueError as e:
        print(e)