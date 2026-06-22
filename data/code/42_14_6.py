import math

class Ellipse:
    def __init__(self, major_axis, minor_axis):
        self.major_axis = major_axis
        self.minor_axis = minor_axis

    def area(self):
        a = self.major_axis / 2
        b = self.minor_axis / 2
        return math.pi * a * b

if __name__ == '__main__':
    ellipse = Ellipse(10, 6)
    print(ellipse.area())