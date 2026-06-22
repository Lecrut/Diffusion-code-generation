import math

class GeometryChecker:
    ELLIPSE_SEMI_MAJOR_AXIS = 5
    ELLIPSE_SEMI_MINOR_AXIS = 3
    RECTANGLE_WIDTH = 10
    RECTANGLE_HEIGHT = 6
    
    @staticmethod
    def area_ellipse(semi_major_axis, semi_minor_axis):
        return math.pi * semi_major_axis * semi_minor_axis
    
    @staticmethod
    def area_rectangle(width, height):
        return width * height
    
    @classmethod
    def check_area_equality(cls):
        ellipse_area = cls.area_ellipse(cls.ELLIPSE_SEMI_MAJOR_AXIS, cls.ELLIPSE_SEMI_MINOR_AXIS)
        rectangle_area = cls.area_rectangle(cls.RECTANGLE_WIDTH, cls.RECTANGLE_HEIGHT)
        return math.isclose(ellipse_area, rectangle_area)

if __name__ == '__main__':
    print(GeometryChecker.check_area_equality())