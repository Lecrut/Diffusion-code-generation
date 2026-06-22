import math

class EllipseCalculator:
    MAJOR_AXIS = 14.0
    MINOR_AXIS = 9.0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_radius_a(self):
        return self.a / 2

    def get_radius_b(self):
        return self.b / 2

    def calculate_area(self):
        return math.pi * self.get_radius_a() * self.get_radius_b()

if __name__ == '__main__':
    calc = EllipseCalculator(EllipseCalculator.MAJOR_AXIS, EllipseCalculator.MINOR_AXIS)
    area_result = calc.calculate_area()
    print(area_result)