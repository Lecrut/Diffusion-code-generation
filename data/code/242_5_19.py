import math

class AreaCalculator:
    def calculate_area_ellipse(self, semi_major_axis, semi_minor_axis):
        return math.pi * semi_major_axis * semi_minor_axis
    
    def calculate_area_triangle(self, base, height):
        return 0.5 * base * height

if __name__ == '__main__':
    calculator = AreaCalculator()
    ellipse_area = calculator.calculate_area_ellipse(5, 3)
    triangle_area = calculator.calculate_area_triangle(10, 4)
    print(f"Ellipse area: {ellipse_area}")
    print(f"Triangle area: {triangle_area}")