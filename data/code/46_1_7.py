class Triangle:
    def __init__(self, side1, side2, side3):
        self._validate_sides(side1, side2, side3)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def _validate_sides(self, a, b, c):
        if not all(isinstance(x, (int, float)) and x > 0 for x in [a, b, c]):
            raise ValueError("All sides must be positive numbers")
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("The given sides do not form a valid triangle")

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    try:
        triangle = Triangle(5, 6, 7)
        print(triangle.perimeter())
    except ValueError as e:
        print(e)