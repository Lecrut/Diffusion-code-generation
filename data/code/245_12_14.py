import math

class AreaChecker:
    def __init__(self, semi_major_axis=5, semi_minor_axis=3, width=10, height=6):
        self.semi_major_axis = semi_major_axis
        self.semi_minor_axis = semi_minor_axis
        self.width = width
        self.height = height

    def area_ellipse(self):
        return math.pi * self.semi_major_axis * self.semi_minor_axis

    def area_rectangle(self):
        return self.width * self.height

    def check_area_equality(self):
        ellipse_area = self.area_ellipse()
        rectangle_area = self.area_rectangle()
        return math.isclose(ellipse_area, rectangle_area)

if __name__ == '__main__':
    checker = AreaChecker()
    print(checker.check_area_equality())