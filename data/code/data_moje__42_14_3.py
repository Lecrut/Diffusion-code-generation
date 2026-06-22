import math

class Ellipse:
    def __init__(self, major_axis, minor_axis):
        if major_axis <= 0 or minor_axis <= 0:
            raise ValueError("Axes must be positive")
        self.major_axis = major_axis
        self.minor_axis = minor_axis

    def area(self):
        return math.pi * (self.major_axis / 2) * (self.minor_axis / 2)

if __name__ == '__main__':
    e = Ellipse(10, 6)
    print(e.area())