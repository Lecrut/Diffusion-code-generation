class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if not (a > 0 and b > 0 and c > 0):
            raise ValueError("All sides must be positive numbers")

    @property
    def perimeter(self):
        return self.a + self.b + self.c

if __name__ == '__main__':
    try:
        triangle1 = Triangle(3, 4, 5)
        print(triangle1.perimeter)
    except ValueError as e:
        print(e)

    try:
        invalid_triangle = Triangle(-1, 4, 5)
        print(invalid_triangle.perimeter)
    except ValueError as e:
        print(e)