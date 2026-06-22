import math

class AreaCalculator:
    SEMICIRCLE_RADIUS = 4
    RECTANGLE_LENGTH = 5
    RECTANGLE_WIDTH = 8
    
    @staticmethod
    def semicircle_area(radius):
        return 0.5 * math.pi * radius ** 2
    
    @staticmethod
    def rectangle_area(length, width):
        return length * width
    
    @classmethod
    def total_area(cls):
        semicircle_a = cls.semicircle_area(cls.SEMICIRCLE_RADIUS)
        rectangle_a = cls.rectangle_area(cls.RECTANGLE_LENGTH, cls.RECTANGLE_WIDTH)
        return semicircle_a + rectangle_a

if __name__ == '__main__':
    result = AreaCalculator.total_area()
    print(result)