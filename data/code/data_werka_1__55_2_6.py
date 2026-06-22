class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if not self._is_valid_triangle():
            raise ValueError('The given side lengths do not form a valid triangle.')

    def _is_valid_triangle(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and (self.b + self.c > self.a)

    def get_perimeter(self):
        return self.a + self.b + self.c
if __name__ == '__main__':
    try:
        t1 = Triangle(3, 4, 5)
        print(f'Perimeter of triangle (3, 4, 5): {t1.get_perimeter()}')
        t2 = Triangle(7, 10, 5)
        print(f'Perimeter of triangle (7, 10, 5): {t2.get_perimeter()}')
        t3 = Triangle(1, 2, 10)
    except ValueError as e:
        print(e)