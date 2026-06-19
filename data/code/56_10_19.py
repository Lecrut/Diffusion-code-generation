import math

class Shapes:
    PI = math.pi
    
    @staticmethod
    def circle_area(radius):
        return Shapes.PI * (radius ** 2)
    
    @staticmethod
    def circle_perimeter(radius):
        return 2 * Shapes.PI * radius
    
    @staticmethod
    def square_area(side_length):
        return side_length ** 2
    
    @staticmethod
    def square_perimeter(side_length):
        return 4 * side_length

if __name__ == '__main__':
    circle_radius = 7.0
    square_side_length = 8.0
    
    circle_area_result = Shapes.circle_area(circle_radius)
    circle_perimeter_result = Shapes.circle_perimeter(circle_radius)
    
    square_area_result = Shapes.square_area(square_side_length)
    square_perimeter_result = Shapes.square_perimeter(square_side_length)
    
    print(f"Circle Area: {circle_area_result}")
    print(f"Circle Perimeter (Circumference): {circle_perimeter_result}")
    print(f"Square Area: {square_area_result}")
    print(f"Square Perimeter: {square_perimeter_result}")