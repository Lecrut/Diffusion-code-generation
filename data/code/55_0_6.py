class Triangle:
    def __init__(self, a, b, c):
        if not self.is_valid_triangle(a, b, c):
            raise ValueError("Invalid triangle sides")
        self.a = a
        self.b = b
        self.c = c

    def is_valid_triangle(self, a, b, c):
        return a + b > c and a + c > b and b + c > a

    def get_perimeter(self):
        return self.a + self.b + self.c

if __name__ == '__main__':
    try:
        triangle = Triangle(3, 4, 5)
        print(triangle.get_perimeter())
    except ValueError as e:
        print(e)