import math
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def calculate_and_print_area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        print(f"The area of the triangle is: {area}")
if __name__ == '__main__':
    triangle1 = Triangle(3, 4, 5)
    triangle1.calculate_and_print_area()
    triangle2 = Triangle(5, 12, 13)
    triangle2.calculate_and_print_area()
    triangle3 = Triangle(6, 8, 10)
    triangle3.calculate_and_print_area()