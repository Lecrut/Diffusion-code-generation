class Ellipse:
    def __init__(self, major_axis, minor_axis):
        self.major_axis = major_axis
        self.minor_axis = minor_axis

    def calculate_area(self):
        import math
        return math.pi * (self.major_axis / 2) * (self.minor_axis / 2)

if __name__ == '__main__':
    sample_major = 10
    sample_minor = 6
    ellipse = Ellipse(sample_major, sample_minor)
    area = ellipse.calculate_area()
    print(area)