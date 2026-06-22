import math

class Ellipse:
    def __init__(self, major_axis, minor_axis):
        self.major_axis = major_axis
        self.minor_axis = minor_axis

    def calculate_area(self):
        return math.pi * (self.major_axis / 2) * (self.minor_axis / 2)

if __name__ == '__main__':
    sample_ellipse = Ellipse(10, 6)
    print(sample_ellipse.calculate_area())