class Triangle:
    def __init__(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle sides")
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        area = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        return area

if __name__ == '__main__':
    try:
        triangle = Triangle(3, 4, 5)
        print(triangle.calculate_area())
    except ValueError as e:
        print(e)