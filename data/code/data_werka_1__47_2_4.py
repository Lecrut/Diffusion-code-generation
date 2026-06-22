import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if not self.is_valid():
            raise ValueError('The given side lengths do not form a valid triangle.')

    def is_valid(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

if __name__ == '__main__':
    t1 = Triangle(3, 4, 5)
    print(t1.calculate_area())

    t2 = Triangle(7, 10, 5)
    print(t2.calculate_area())