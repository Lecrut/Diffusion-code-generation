import math

class Ellipse:
    def __init__(self, major_axis, minor_axis):
        self.major_axis = major_axis
        self.minor_axis = minor_axis

    def calculate_area(self):
        return math.pi * (self.major_axis / 2) * (self.minor_axis / 2)

if __name__ == '__main__':
    ellipse = Ellipse(10, 6)
    area = ellipse.calculate_area()
    print(area)