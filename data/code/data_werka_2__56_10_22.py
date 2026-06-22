import math

class Shapes:
    def __init__(self, circle_radius=0, square_side_length=0):
        self.circle_radius = circle_radius
        self.square_side_length = square_side_length
    
    def calculate_circle_area(self):
        return math.pi * (self.circle_radius ** 2)
    
    def calculate_circle_perimeter(self):
        return 2 * math.pi * self.circle_radius
    
    def calculate_square_area(self):
        return self.square_side_length ** 2
    
    def calculate_square_perimeter(self):
        return 4 * self.square_side_length

if __name__ == '__main__':
    circle_radius = 7
    square_side_length = 15
    shape = Shapes(circle_radius=circle_radius, square_side_length=square_side_length)
    
    circle_area = shape.calculate_circle_area()
    circle_perimeter = shape.calculate_circle_perimeter()
    square_area = shape.calculate_square_area()
    square_perimeter = shape.calculate_square_perimeter()
    
    print(f"Circle with radius {circle_radius}:")
    print(f"Area: {circle_area}")
    print(f"Perimeter: {circle_perimeter}")
    
    print(f"\nSquare with side length {square_side_length}:")
    print(f"Area: {square_area}")
    print(f"Perimeter: {square_perimeter}")