import math

class GeometryCalculator:
    SEMI_MAJOR_AXIS = 5
    SEMI_MINOR_AXIS = 3
    BASE = 10
    HEIGHT = 4

    @staticmethod
    def calculate_area_ellipse(semi_major_axis, semi_minor_axis):
        return math.pi * semi_major_axis * semi_minor_axis

    @staticmethod
    def calculate_area_triangle(base, height):
        return 0.5 * base * height

if __name__ == '__main__':
    ellipse_area = GeometryCalculator.calculate_area_ellipse(GeometryCalculator.SEMI_MAJOR_AXIS, GeometryCalculator.SEMI_MINOR_AXIS)
    triangle_area = GeometryCalculator.calculate_area_triangle(GeometryCalculator.BASE, GeometryCalculator.HEIGHT)
    print(f"Ellipse area: {ellipse_area}")
    print(f"Triangle area: {triangle_area}")