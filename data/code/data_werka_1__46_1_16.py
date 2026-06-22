class Triangle:
    MIN_SIDE_LENGTH = 1

    def __init__(self, side1, side2, side3):
        self._validate_sides(side1, side2, side3)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @staticmethod
    def _validate_sides(a, b, c):
        if not (a > Triangle.MIN_SIDE_LENGTH and b > Triangle.MIN_SIDE_LENGTH and c > Triangle.MIN_SIDE_LENGTH):
            raise ValueError("Side lengths must be greater than 0")
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("The given sides do not form a valid triangle")

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    try:
        triangle = Triangle(6, 8, 10)
        print(triangle.perimeter())
    except ValueError as e:
        print(e)