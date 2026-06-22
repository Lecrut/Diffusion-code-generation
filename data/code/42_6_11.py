import math

class Ellipse:
    def __init__(self, semi_major_axis, semi_minor_axis):
        if semi_major_axis <= 0 or semi_minor_axis <= 0:
            raise ValueError("Axes must be positive")
        self.a = semi_major_axis
        self.b = semi_minor_axis

    def area(self):
        return math.pi * self.a * self.b

if __name__ == '__main__':
    ellipse = Ellipse(4, 2)
    print(ellipse.area())