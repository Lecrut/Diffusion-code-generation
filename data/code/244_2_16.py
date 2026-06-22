import math

class Ellipse:
    def __init__(self, semi_major_axis, semi_minor_axis):
        self.semi_major_axis = semi_major_axis
        self.semi_minor_axis = semi_minor_axis
    
    def area(self):
        return math.pi * self.semi_major_axis * self.semi_minor_axis

class EllipseCalculator:
    def calculate_total_area(self, ellipse1, ellipse2):
        return ellipse1.area() + ellipse2.area()

if __name__ == '__main__':
    ellipse_a = Ellipse(3, 2)
    ellipse_b = Ellipse(4, 1)
    calculator = EllipseCalculator()
    total_area = calculator.calculate_total_area(ellipse_a, ellipse_b)
    print(total_area)