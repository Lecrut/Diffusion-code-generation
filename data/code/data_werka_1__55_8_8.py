class Triangle:

    def __init__(self, side1, side2, side3):
        self._validate_sides(side1, side2, side3)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def _validate_sides(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError('Side lengths must be positive')
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError('Invalid triangle side lengths')

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3
if __name__ == '__main__':
    try:
        triangle = Triangle(3, 4, 5)
        print(triangle.get_perimeter())
    except ValueError as e:
        print(e)
    try:
        invalid_triangle = Triangle(1, 2, 4)
    except ValueError as e:
        print(e)
    try:
        another_invalid_triangle = Triangle(-1, 2, 3)
    except ValueError as e:
        print(e)