import math

class EllipseCalculator:
    @staticmethod
    def ellipse_area(a, b):
        return math.pi * a * b
    
    @staticmethod
    def combined_areas(axes1, axes2):
        area1 = EllipseCalculator.ellipse_area(*axes1)
        area2 = EllipseCalculator.ellipse_area(*axes2)
        return area1 + area2

if __name__ == '__main__':
    total_area = EllipseCalculator.combined_areas((3, 4), (5, 6))
    print(total_area)