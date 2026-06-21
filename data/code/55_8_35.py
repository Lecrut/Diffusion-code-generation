class Triangle:

    def __init__(self, side_a, side_b, side_c):
        self._validate_sides(side_a, side_b, side_c)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def _validate_sides(self, a, b, c):
        if not all((isinstance(x, (int, float)) and x > 0 for x in [a, b, c])):
            raise ValueError('All side lengths must be positive numbers.')

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
if __name__ == '__main__':
    try:
        triangle = Triangle(5, 12, 13)
        print(triangle.perimeter())
        print(f'Side A: {triangle.side_a}, Side B: {triangle.side_b}, Side C: {triangle.side_c}')
    except ValueError as e:
        print(e)