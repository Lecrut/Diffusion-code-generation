import math

class GeometryCalculator:
    def __init__(self):
        self.semi_major_axis = 5
        self.semi_minor_axis = 3
        self.base = 10
        self.height = 4
    
    def calculate_area_ellipse(self, semi_major_axis=None, semi_minor_axis=None):
        if semi_major_axis is None:
            semi_major_axis = self.semi_major_axis
        if semi_minor_axis is None:
            semi_minor_axis = self.semi_minor_axis
        return math.pi * semi_major_axis * semi_minor_axis
    
    def calculate_area_triangle(self, base=None, height=None):
        if base is None:
            base = self.base
        if height is None:
            height = self.height
        return 0.5 * base * height

if __name__ == '__main__':
    calculator = GeometryCalculator()
    ellipse_area = calculator.calculate_area_ellipse()
    triangle_area = calculator.calculate_area_triangle()
    print(f"Ellipse area: {ellipse_area}")
    print(f"Triangle area: {triangle_area}")