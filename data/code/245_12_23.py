import math

class AreaCalculator:
    @staticmethod
    def area_ellipse(semi_major_axis, semi_minor_axis):
        return math.pi * semi_major_axis * semi_minor_axis
    
    @staticmethod
    def area_rectangle(width, height):
        return width * height
    
    @staticmethod
    def check_area_equality(ellipse_semi_major_axis, ellipse_semi_minor_axis, rectangle_width, rectangle_height):
        ellipse_area = AreaCalculator.area_ellipse(ellipse_semi_major_axis, ellipse_semi_minor_axis)
        rectangle_area = AreaCalculator.area_rectangle(rectangle_width, rectangle_height)
        return math.isclose(ellipse_area, rectangle_area)

if __name__ == '__main__':
    print(AreaCalculator.check_area_equality(5, 3, 10, 6))