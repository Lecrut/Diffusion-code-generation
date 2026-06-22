import math

class EllipseCalculator:
    @staticmethod
    def ellipse_area(a, b):
        return math.pi * a * b
    
    @staticmethod
    def area_ratio():
        semi_major_1 = 5
        semi_minor_1 = 3
        semi_major_2 = 4
        semi_minor_2 = 2
        
        area_1 = EllipseCalculator.ellipse_area(semi_major_1, semi_minor_1)
        area_2 = EllipseCalculator.ellipse_area(semi_major_2, semi_minor_2)
        
        if area_1 > area_2:
            return area_1 / area_2
        else:
            return area_2 / area_1

if __name__ == '__main__':
    print(EllipseCalculator.area_ratio())