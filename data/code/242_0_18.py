import math

class AreaCalculator:
    def __init__(self, circle_radius, square_side_length):
        self.circle_radius = circle_radius
        self.square_side_length = square_side_length
    
    def calculate_circle_area(self):
        return math.pi * (self.circle_radius ** 2)
    
    def calculate_square_area(self):
        return self.square_side_length ** 2

if __name__ == '__main__':
    calculator = AreaCalculator(5, 6)
    circle_area = calculator.calculate_circle_area()
    square_area = calculator.calculate_square_area()
    print(f"Circle area: {circle_area}")
    print(f"Square area: {square_area}")
    if circle_area > square_area:
        print("The circle has a larger area.")
    else:
        print("The square has a larger or equal area.")