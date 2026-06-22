import math

class ShapeAreaComparer:
    CIRCLE_RADIUS = 5
    RECTANGLE_LENGTH = 10
    RECTANGLE_WIDTH = 7
    
    @staticmethod
    def calculate_circle_area(radius):
        return math.pi * radius ** 2
    
    @staticmethod
    def calculate_rectangle_area(length, width):
        return length * width
    
    @staticmethod
    def compare_areas():
        circle_area = ShapeAreaComparer.calculate_circle_area(ShapeAreaComparer.CIRCLE_RADIUS)
        rectangle_area = ShapeAreaComparer.calculate_rectangle_area(ShapeAreaComparer.RECTANGLE_LENGTH, ShapeAreaComparer.RECTANGLE_WIDTH)
        
        if circle_area > rectangle_area:
            print(f"The circle with radius {ShapeAreaComparer.CIRCLE_RADIUS} has a larger area: {circle_area}")
        elif circle_area < rectangle_area:
            print(f"The rectangle with dimensions {ShapeAreaComparer.RECTANGLE_LENGTH}x{ShapeAreaComparer.RECTANGLE_WIDTH} has a larger area: {rectangle_area}")
        else:
            print("Both shapes have the same area.")

if __name__ == '__main__':
    ShapeAreaComparer.compare_areas()