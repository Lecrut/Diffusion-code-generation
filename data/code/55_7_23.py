class Triangle:

    def __init__(self, side1, side2, side3):
        self._validate_sides(side1, side2, side3)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def _validate_sides(self, a, b, c):
        if not all((isinstance(x, (int, float)) and x > 0 for x in [a, b, c])):
            raise ValueError('Side lengths must be positive numbers')
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError('The given sides do not form a valid triangle')

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3
if __name__ == '__main__':
    try:
        side_a = 5
        side_b = 12
        side_c = 13
        triangle = Triangle(side_a, side_b, side_c)
        print('Perimeter:', triangle.get_perimeter())
        side_x = 7
        side_y = 24
        side_z = 25
        another_triangle = Triangle(side_x, side_y, side_z)
        print('Another Perimeter:', another_triangle.get_perimeter())
    except ValueError as e:
        print(e)