import math

class EllipseGeometry:
    def __init__(self, major_axis, minor_axis):
        if major_axis <= 0:
            raise ValueError("Major axis must be greater than zero")
        if minor_axis <= 0:
            raise ValueError("Minor axis must be greater than zero")
        self.major_axis = major_axis
        self.minor_axis = minor_axis
        self._half_major = major_axis / 2.0
        self._half_minor = minor_axis / 2.0

    def get_area(self):
        return math.pi * self._half_major * self._half_minor

def run_deterministic_test():
    test_major = 14.0
    test_minor = 8.0
    ellipse = EllipseGeometry(test_major, test_minor)
    result = ellipse.get_area()
    print(result)

if __name__ == '__main__':
    run_deterministic_test()