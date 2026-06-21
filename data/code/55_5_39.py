class Triangle:
    MIN_SIDE = 1

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.validate_sides()

    @staticmethod
    def validate_side_length(side):
        if side < Triangle.MIN_SIDE:
            raise ValueError("Side length must be at least 1")

    def validate_sides(self):
        Triangle.validate_side_length(self.side1)
        Triangle.validate_side_length(self.side2)
        Triangle.validate_side_length(self.side3)

        if not (self.side1 + self.side2 > self.side3 and
                self.side1 + self.side3 > self.side2 and
                self.side2 + self.side3 > self.side1):
            raise ValueError("Invalid triangle sides")

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    try:
        triangle = Triangle(3, 4, 5)
        print(triangle.perimeter())
    except ValueError as e:
        print(e)