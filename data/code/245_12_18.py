import math

class ShapeAreas:
    def __init__(self, ellipse_semi_major_axis=5, ellipse_semi_minor_axis=3, rectangle_width=10, rectangle_height=6):
        self.ellipse_semi_major_axis = ellipse_semi_major_axis
        self.ellipse_semi_minor_axis = ellipse_semi_minor_axis
        self.rectangle_width = rectangle_width
        self.rectangle_height = rectangle_height

    def area_ellipse(self):
        return math.pi * self.ellipse_semi_major_axis * self.ellipse_semi_minor_axis

    def area_rectangle(self):
        return self.rectangle_width * self.rectangle_height

    def check_area_equality(self):
        ellipse_area = self.area_ellipse()
        rectangle_area = self.area_rectangle()
        return math.isclose(ellipse_area, rectangle_area)

if __name__ == '__main__':
    shape_areas = ShapeAreas()
    print(shape_areas.check_area_equality())