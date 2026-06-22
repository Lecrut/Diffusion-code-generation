import math

class GeometryCalculator:
    @staticmethod
    def calculate_circle_area(radius):
        return math.pi * radius ** 2
    
    @staticmethod
    def calculate_square_area(side_length):
        return side_length ** 2

if __name__ == '__main__':
    circle_radius = 5
    square_side_length = 6
    circle_area = GeometryCalculator.calculate_circle_area(circle_radius)
    square_area = GeometryCalculator.calculate_square_area(square_side_length)
    print(f"Circle area: {circle_area}")
    print(f"Square area: {square_area}")