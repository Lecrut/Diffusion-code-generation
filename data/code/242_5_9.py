import math

class GeometryCalculator:
    def __init__(self):
        self.ellipse_params = (5, 3)
        self.triangle_params = (10, 4)

    def calculate_area_ellipse(self, semi_major_axis, semi_minor_axis):
        return math.pi * semi_major_axis * semi_minor_axis

    def calculate_area_triangle(self, base, height):
        return 0.5 * base * height

if __name__ == '__main__':
    calculator = GeometryCalculator()
    ellipse_area = calculator.calculate_area_ellipse(*calculator.ellipse_params)
    triangle_area = calculator.calculate_area_triangle(*calculator.triangle_params)
    print(f"Ellipse area: {ellipse_area}")
    print(f"Triangle area: {triangle_area}")