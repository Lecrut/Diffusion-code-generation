import math

class EllipseCalculator:
    def __init__(self, semi_major, semi_minor):
        self.semi_major = semi_major
        self.semi_minor = semi_minor

    def get_area(self):
        return math.pi * self.semi_major * self.semi_minor

    def get_circumference_approximation(self):
        return math.pi * 3 * (self.semi_major + self.semi_minor)

if __name__ == '__main__':
    major_axis = 10
    minor_axis = 6
    calculator = EllipseCalculator(major_axis, minor_axis)
    print(calculator.get_area())
    print(calculator.get_circumference_approximation())