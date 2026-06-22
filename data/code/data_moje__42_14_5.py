import math

class EllipseGeometry:
    def __init__(self, major_axis_length, minor_axis_length):
        if major_axis_length <= 0 or minor_axis_length <= 0:
            raise ValueError("Axis lengths must be positive numbers")
        self.major_axis_length = major_axis_length
        self.minor_axis_length = minor_axis_length

    def get_semi_major_axis(self):
        return self.major_axis_length / 2.0

    def get_semi_minor_axis(self):
        return self.minor_axis_length / 2.0

    def calculate_area(self):
        semi_major = self.get_semi_major_axis()
        semi_minor = self.get_semi_minor_axis()
        return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    shape = EllipseGeometry(12.0, 8.0)
    area_result = shape.calculate_area()
    print(area_result)
    semi_major = shape.get_semi_major_axis()
    print(semi_major)
    semi_minor = shape.get_semi_minor_axis()
    print(semi_minor)