import math

def area_of_ellipse(a, b):
    return math.pi * a * b

class Ellipse:
    def __init__(self, semi_major_axis, semi_minor_axis):
        if semi_major_axis <= 0 or semi_minor_axis <= 0:
            raise ValueError("Semi-major and semi-minor axes must be positive numbers")
        self.semi_major_axis = semi_major_axis
        self.semi_minor_axis = semi_minor_axis

    def get_area(self):
        return area_of_ellipse(self.semi_major_axis, self.semi_minor_axis)

if __name__ == '__main__':
    ellipse1 = Ellipse(3, 2)
    ellipse2 = Ellipse(4, 1)
    total_area = ellipse1.get_area() + ellipse2.get_area()
    print(total_area)