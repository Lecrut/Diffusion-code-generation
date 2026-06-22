import math

class Ellipse:
    def __init__(self, semi_major, semi_minor):
        self.semi_major = semi_major
        self.semi_minor = semi_minor

    def area(self):
        return math.pi * self.semi_major * self.semi_minor

class AreaCalculator:
    def calculate_total_area(self, ellipse1, ellipse2):
        return ellipse1.area() + ellipse2.area()

if __name__ == '__main__':
    ellipse_a = Ellipse(3, 2)
    ellipse_b = Ellipse(4, 1)
    calculator = AreaCalculator()
    total_area = calculator.calculate_total_area(ellipse_a, ellipse_b)
    print(total_area)