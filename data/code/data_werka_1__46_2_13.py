class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self._validate_sides()

    @staticmethod
    def _is_valid_triangle(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def _validate_sides(self):
        if not all(isinstance(x, (int, float)) and x > 0 for x in [self.a, self.b, self.c]):
            raise ValueError("Side lengths must be positive numbers.")
        if not Triangle._is_valid_triangle(self.a, self.b, self.c):
            raise ValueError("The given side lengths do not form a valid triangle.")

    def calculate_perimeter(self):
        return self.a + self.b + self.c

if __name__ == '__main__':
    try:
        t = Triangle(3, 4, 5)
        perimeter = t.calculate_perimeter()
        print(perimeter)
    except ValueError as e:
        print(e)