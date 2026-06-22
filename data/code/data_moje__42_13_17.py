import math

class EllipseCalculator:
    def __init__(self, semi_major_axis, semi_minor_axis):
        self.a = semi_major_axis
        self.b = semi_minor_axis

    def get_area(self):
        return math.pi * self.a * self.b

    def get_semimajor(self):
        return self.a

    def get_semiminor(self):
        return self.b

if __name__ == '__main__':
    a_value = 12.5
    b_value = 7.3
    calculator = EllipseCalculator(a_value, b_value)
    print(calculator.get_area())
    print(calculator.get_semimajor())
    print(calculator.get_semiminor())