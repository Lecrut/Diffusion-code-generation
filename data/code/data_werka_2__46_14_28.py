class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self._validate_sides()

    def _validate_sides(self):
        if not all(isinstance(side, (int, float)) for side in [self.side1, self.side2, self.side3]):
            raise ValueError("All sides must be numbers.")
        if any(side <= 0 for side in [self.side1, self.side2, self.side3]):
            raise ValueError("Side lengths must be positive numbers.")

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    triangle = Triangle(6, 8, 10)
    print(triangle.perimeter())