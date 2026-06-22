class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def perimeter(self):
        return self.a + self.b + self.c

if __name__ == '__main__':
    triangle = Triangle(3.0, 4.0, 5.0)
    print(triangle.perimeter)