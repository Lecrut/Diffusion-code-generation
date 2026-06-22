import math

ELLIPSE_UNITS = {
    'standard': {'major': 12.0, 'minor': 8.0},
    'large': {'major': 20.0, 'minor': 15.0},
    'small': {'major': 5.0, 'minor': 3.0}
}

class EllipseGeometry:
    def __init__(self, major_axis, minor_axis):
        self.major_axis = major_axis
        self.minor_axis = minor_axis

    def get_semi_axes(self):
        return self.major_axis / 2, self.minor_axis / 2

    def calculate_area(self):
        semi_major, semi_minor = self.get_semi_axes()
        return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    test_data = ELLIPSE_UNITS['standard']
    shape = EllipseGeometry(test_data['major'], test_data['minor'])
    print(shape.calculate_area())