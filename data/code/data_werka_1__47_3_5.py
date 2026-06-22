class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if not self.is_valid_triangle():
            raise ValueError("Invalid triangle sides")

    def is_valid_triangle(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

    @staticmethod
    def calculate_area(a, b, c):
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area

    def get_area(self):
        return Triangle.calculate_area(self.a, self.b, self.c)

if __name__ == '__main__':
    try:
        triangle = Triangle(3, 4, 5)
        print(triangle.get_area())
    except ValueError as e:
        print(e)