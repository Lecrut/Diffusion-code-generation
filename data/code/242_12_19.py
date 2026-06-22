import math

class EllipseAreaCalculator:
    @staticmethod
    def ellipse_area(a, b):
        return math.pi * a * b
    
    @classmethod
    def area_ratio(cls, semi_major_1, semi_minor_1, semi_major_2, semi_minor_2):
        area_1 = cls.ellipse_area(semi_major_1, semi_minor_1)
        area_2 = cls.ellipse_area(semi_major_2, semi_minor_2)
        
        if area_1 > area_2:
            return area_1 / area_2
        else:
            return area_2 / area_1

if __name__ == '__main__':
    calculator = EllipseAreaCalculator()
    print(calculator.area_ratio(5, 3, 4, 2))