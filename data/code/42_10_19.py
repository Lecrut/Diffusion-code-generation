import math

class EllipseCalculator:
    def __init__(self, major_axis, minor_axis):
        self.major_axis = self._validate(major_axis)
        self.minor_axis = self._validate(minor_axis)

    def _validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Axis length must be a number.")
        if value <= 0:
            raise ValueError("Axis length must be positive.")
        return value

    def get_area(self):
        semi_major = self.major_axis / 2.0
        semi_minor = self.minor_axis / 2.0
        return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    calculator = EllipseCalculator(20, 12)
    print(calculator.get_area())