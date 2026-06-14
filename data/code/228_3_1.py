class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def calculate_and_print_area(self):
        s = (self.a + self.b + self.c) / 2
        area = (s - self.a) * (s - self.b) * (s - self.c) ** 2
        print(f"The area of the triangle is: {area}")
if __name__ == '__main__':
    t = Triangle(3, 4, 5)
    t.calculate_and_print_area()