class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self._is_valid = self._validate_triangle(a, b, c)
    def _validate_triangle(self, a, b, c):
        if a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0:
            return True
        return False
    def get_perimeter(self):
        if not self._is_valid:
            raise ValueError("The given side lengths do not form a valid triangle.")
        return self.a + self.b + self.c
if __name__ == '__main__':
    try:
        t1 = Triangle(3, 4, 5)
        print(f"Perimeter of triangle (3, 4, 5): {t1.get_perimeter()}")
        t2 = Triangle(1, 2, 5)
        print(f"Perimeter of triangle (1, 2, 5): {t2.get_perimeter()}")
        t3 = Triangle(6, 8, 10)
        print(f"Perimeter of triangle (6, 8, 10): {t3.get_perimeter()}")
    except ValueError as e:
        print(f"Error: {e}")