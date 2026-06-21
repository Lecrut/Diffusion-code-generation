class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.validate_sides()

    def validate_sides(self):
        if not (isinstance(self.side1, (int, float)) and
                isinstance(self.side2, (int, float)) and
                isinstance(self.side3, (int, float))):
            raise ValueError("Sides must be numbers")
        if self.side1 <= 0 or self.side2 <= 0 or self.side3 <= 0:
            raise ValueError("Sides must be positive")
        if not (self.side1 + self.side2 > self.side3 and
                self.side1 + self.side3 > self.side2 and
                self.side2 + self.side3 > self.side1):
            raise ValueError("Invalid triangle sides")

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    try:
        triangle = Triangle(6, 8, 10)
        print(triangle.perimeter())
    except ValueError as e:
        print(e)