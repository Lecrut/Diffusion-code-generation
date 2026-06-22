class Triangle:
    def __init__(self, a, b, c):
        if not (a > 0 and b > 0 and c > 0):
            raise ValueError("Sides must be positive numbers.")
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

if __name__ == '__main__':
    try:
        triangle = Triangle(3.0, 4.0, 5.0)
        print(triangle.perimeter())
    except ValueError as e:
        print(e)