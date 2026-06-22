import math

class Ellipse:
    def __init__(self, major_axis, minor_axis):
        self.major_axis = major_axis
        self.minor_axis = minor_axis

    def calculate_area(self):
        a = self.major_axis / 2
        b = self.minor_axis / 2
        return math.pi * a * b

if __name__ == '__main__':
    sample_ellipse = Ellipse(10, 6)
    print(sample_ellipse.calculate_area())