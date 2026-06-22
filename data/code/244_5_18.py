import math

class AreaCalculator:
    SEMICIRCLE_RADIUS = 4
    RECTANGLE_LENGTH = 5
    RECTANGLE_WIDTH = 8
    
    @staticmethod
    def calculate_semicircle_area():
        return 0.5 * math.pi * (AreaCalculator.SEMICIRCLE_RADIUS ** 2)
    
    @staticmethod
    def calculate_rectangle_area():
        return AreaCalculator.RECTANGLE_LENGTH * AreaCalculator.RECTANGLE_WIDTH
    
    @staticmethod
    def add_two_areas(area1, area2):
        return area1 + area2

if __name__ == '__main__':
    semicircle_area = AreaCalculator.calculate_semicircle_area()
    rectangle_area = AreaCalculator.calculate_rectangle_area()
    total_area = AreaCalculator.add_two_areas(semicircle_area, rectangle_area)
    print(total_area)