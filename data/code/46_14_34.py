class Triangle:
    MIN_SIDE_LENGTH = 1

    @staticmethod
    def validate_side_length(side):
        if side < Triangle.MIN_SIDE_LENGTH:
            raise ValueError("Side lengths must be at least {}.".format(Triangle.MIN_SIDE_LENGTH))

    def __init__(self, side1, side2, side3):
        self.validate_side_length(side1)
        self.validate_side_length(side2)
        self.validate_side_length(side3)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    triangle = Triangle(6, 8, 10)
    print(triangle.perimeter())