class Triangle:
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Side lengths must be positive")
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError("Invalid triangle sides")
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

if __name__ == '__main__':
    t = Triangle(3, 4, 5)
    print(t.perimeter())