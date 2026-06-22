import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_square_area(side_length):
    return side_length ** 2

class AreaCalculator:
    def __init__(self, circle_radius, square_side_length):
        self.circle_radius = circle_radius
        self.square_side_length = square_side_length
    
    def get_circle_area(self):
        return calculate_circle_area(self.circle_radius)
    
    def get_square_area(self):
        return calculate_square_area(self.square_side_length)

if __name__ == '__main__':
    circle_radius = 5
    square_side_length = 6
    calculator = AreaCalculator(circle_radius, square_side_length)
    circ_area = calculator.get_circle_area()
    squr_area = calculator.get_square_area()
    print(f"Circle Radius: {circle_radius}")
    print(f"Square Side Length: {square_side_length}")
    print("-" * 30)
    print(f"Area of the Circle: {circ_area}")
    print(f"Area of the Square: {squr_area}")
    if circ_area > squr_area:
        print("The circle has a larger area.")