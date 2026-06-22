import math

class Ellipse:
    def __init__(self, major_axis, minor_axis):
        if major_axis <= 0 or minor_axis <= 0:
            raise ValueError("Axes must be positive")
        self.major_axis = major_axis
        self.minor_axis = minor_axis

    def semi_major(self):
        return self.major_axis / 2

    def semi_minor(self):
        return self.minor_axis / 2

    def area(self):
        return math.pi * self.semi_major() * self.semi_minor()

    def perimeter_approx(self):
        a = self.semi_major()
        b = self.semi_minor()
        return math.pi * math.sqrt(2 * (a**2 + b**2))

if __name__ == '__main__':
    ellipse = Ellipse(12, 8)
    print(ellipse.area())
    print(ellipse.perimeter_approx())