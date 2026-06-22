import math

class GeometryCalculator:
    def __init__(self):
        self.semi_major_axis = 5
        self.semi_minor_axis = 3
        self.base = 10
        self.height = 4
    
    def calculate_area_ellipse(self):
        return math.pi * self.semi_major_axis * self.semi_minor_axis
    
    def calculate_area_triangle(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    calculator = GeometryCalculator()
    ellipse_area = calculator.calculate_area_ellipse()
    triangle_area = calculator.calculate_area_triangle()
    print(f"Ellipse area: {ellipse_area}")
    print(f"Triangle area: {triangle_area}")