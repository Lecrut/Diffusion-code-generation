class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def validate_sides(a, b, c):
        return a > 0 and b > 0 and c > 0

    def perimeter(self):
        return self.a + self.b + self.c

if __name__ == '__main__':
    sides = (3.0, 4.0, 5.0)
    if Triangle.validate_sides(*sides):
        triangle = Triangle(*sides)
        print(triangle.perimeter())
    else:
        print("Invalid side lengths")