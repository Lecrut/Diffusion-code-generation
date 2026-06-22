class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if not self._validate_triangle():
            raise ValueError('The given side lengths do not form a valid triangle.')

    def _validate_triangle(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and (self.b + self.c > self.a)

    def get_perimeter(self):
        return self.a + self.b + self.c
if __name__ == '__main__':
    try:
        triangle1 = Triangle(3, 4, 5)
        print(f'Perimeter of triangle (3, 4, 5): {triangle1.get_perimeter()}')
        triangle2 = Triangle(7, 10, 5)
        print(f'Perimeter of triangle (7, 10, 5): {triangle2.get_perimeter()}')
        invalid_triangle = Triangle(1, 2, 10)
    except ValueError as e:
        print(e)