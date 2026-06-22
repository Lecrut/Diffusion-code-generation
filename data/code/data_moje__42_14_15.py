import math

class Ellipse:
    def __init__(self, major_axis, minor_axis):
        self.major_axis = major_axis
        self.minor_axis = minor_axis

    def calculate_area(self):
        semi_major = self.major_axis / 2
        semi_minor = self.minor_axis / 2
        return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    ellipse = Ellipse(10.0, 6.0)
    area = ellipse.calculate_area()
    print(area)