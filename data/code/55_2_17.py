class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if not self._is_valid_triangle(a, b, c):
            raise ValueError("The given side lengths do not form a valid triangle.")

    def _is_valid_triangle(self, a, b, c):
        return a + b > c and a + c > b and b + c > a

    def get_perimeter(self):
        return self.a + self.b + self.c

if __name__ == '__main__':
    try:
        t1 = Triangle(3, 4, 5)
        print(f"Perimeter of triangle (3, 4, 5): {t1.get_perimeter()}")
    except ValueError as e:
        print(e)

    try:
        t2 = Triangle(1, 2, 10)
        print(f"Perimeter of triangle (1, 2, 10): {t2.get_perimeter()}")
    except ValueError as e:
        print(e)