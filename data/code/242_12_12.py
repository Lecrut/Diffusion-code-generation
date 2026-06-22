import math

def ellipse_area(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Semi-major and semi-minor axes must be positive numbers.")
    return math.pi * a * b

class EllipseAreaCalculator:
    def __init__(self, semi_major_1, semi_minor_1, semi_major_2, semi_minor_2):
        self.semi_major_1 = semi_major_1
        self.semi_minor_1 = semi_minor_1
        self.semi_major_2 = semi_major_2
        self.semi_minor_2 = semi_minor_2

    def calculate_areas(self):
        return ellipse_area(self.semi_major_1, self.semi_minor_1), ellipse_area(self.semi_major_2, self.semi_minor_2)

    def ratio_of_larger_to_smaller_area(self):
        area_1, area_2 = self.calculate_areas()
        if area_1 > area_2:
            return area_1 / area_2
        else:
            return area_2 / area_1

if __name__ == '__main__':
    calculator = EllipseAreaCalculator(5, 3, 4, 2)
    print(calculator.ratio_of_larger_to_smaller_area())