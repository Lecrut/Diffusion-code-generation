class Triangle:
    MIN_SIDE_LENGTH = 1

    def __init__(self, side1, side2, side3):
        self._validate_sides(side1, side2, side3)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @staticmethod
    def _validate_sides(a, b, c):
        if any(x <= Triangle.MIN_SIDE_LENGTH for x in (a, b, c)):
            raise ValueError("Side lengths must be greater than zero")
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("The given sides do not form a valid triangle")

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    try:
        sample_triangle = Triangle(9, 12, 15)
        print(sample_triangle.get_perimeter())
    except ValueError as e:
        print(e)