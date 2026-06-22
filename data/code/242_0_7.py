import math

class GeometryCalculator:
    CIRCLE_RADIUS = 5
    SQUARE_SIDE_LENGTH = 6
    
    @staticmethod
    def calculate_area_circle(radius):
        return math.pi * radius ** 2
    
    @staticmethod
    def calculate_area_square(side_length):
        return side_length ** 2
    
if __name__ == '__main__':
    circle_area = GeometryCalculator.calculate_area_circle(GeometryCalculator.CIRCLE_RADIUS)
    square_area = GeometryCalculator.calculate_area_square(GeometryCalculator.SQUARE_SIDE_LENGTH)
    
    print(f"Circle area: {circle_area}")
    print(f"Square area: {square_area}")
    
    if circle_area > square_area:
        print("The circle has a larger area.")