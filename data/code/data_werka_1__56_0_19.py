import math

class ShapeCalculator:
    PI = math.pi
    
    @staticmethod
    def circle_area(radius):
        return ShapeCalculator.PI * radius ** 2
    
    @staticmethod
    def circle_perimeter(radius):
        return 2 * ShapeCalculator.PI * radius
    
    @staticmethod
    def square_area(side_length):
        return side_length ** 2
    
    @staticmethod
    def square_perimeter(side_length):
        return 4 * side_length

if __name__ == '__main__':
    circle_radius = 7.0
    square_side_length = 6.0
    
    circle_area_result = ShapeCalculator.circle_area(circle_radius)
    circle_perimeter_result = ShapeCalculator.circle_perimeter(circle_radius)
    square_area_result = ShapeCalculator.square_area(square_side_length)
    square_perimeter_result = ShapeCalculator.square_perimeter(square_side_length)
    
    print(f"Circle Area: {circle_area_result}")
    print(f"Circle Perimeter: {circle_perimeter_result}")
    print(f"Square Area: {square_area_result}")
    print(f"Square Perimeter: {square_perimeter_result}")