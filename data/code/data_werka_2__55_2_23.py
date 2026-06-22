class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self._validate_sides()

    def _validate_sides(self):
        if not (self._is_greater_than_sum(self.a, self.b, self.c) and self._is_greater_than_sum(self.a, self.c, self.b) and self._is_greater_than_sum(self.b, self.c, self.a)):
            raise ValueError('The given side lengths do not form a valid triangle.')

    def _is_greater_than_sum(self, x, y, z):
        return x + y > z

    def get_perimeter(self):
        return self.a + self.b + self.c
if __name__ == '__main__':
    try:
        t1 = Triangle(3, 4, 5)
        print(f'Perimeter of triangle (3, 4, 5): {t1.get_perimeter()}')
        t2 = Triangle(6, 8, 10)
        print(f'Perimeter of triangle (6, 8, 10): {t2.get_perimeter()}')
        t3 = Triangle(1, 1, 2)
    except ValueError as e:
        print(e)