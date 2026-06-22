class TriangleValidator:
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Sides must be positive numbers")
        if not all(isinstance(x, (int, float)) for x in (a, b, c)):
            raise TypeError("Sides must be numeric")
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

if __name__ == '__main__':
    try:
        t1 = TriangleValidator(3, 4, 5)
        print(t1.is_valid())
        t2 = TriangleValidator(1, 2, 3)
        print(t2.is_valid())
        t3 = TriangleValidator(-1, 2, 3)
        print(t3.is_valid())
    except (ValueError, TypeError) as e:
        print(str(e))