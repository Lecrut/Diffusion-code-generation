class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

if __name__ == '__main__':
    triangle1 = Triangle(3, 4, 5)
    print("Perimeter of triangle1:", triangle1.perimeter())

    triangle2 = Triangle(6, 8, 10)
    print("Perimeter of triangle2:", triangle2.perimeter())