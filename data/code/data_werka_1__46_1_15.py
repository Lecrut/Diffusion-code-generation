class Triangle:

    def __init__(self, side1, side2, side3):
        self._validate_sides(side1, side2, side3)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def _validate_sides(self, a, b, c):
        if not (a > 0 and b > 0 and (c > 0)):
            raise ValueError('All sides must be positive numbers.')
        if not (a + b > c and a + c > b and (b + c > a)):
            raise ValueError('The given sides do not form a valid triangle.')

    def perimeter(self):
        return self.side1 + self.side2 + self.side3
if __name__ == '__main__':
    try:
        side_a = 5
        side_b = 6
        side_c = 7
        triangle = Triangle(side_a, side_b, side_c)
        print(triangle.perimeter())
    except ValueError as e:
        print(e)