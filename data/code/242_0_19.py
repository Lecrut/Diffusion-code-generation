import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_square_area(side_length):
    return side_length ** 2

if __name__ == '__main__':
    circle_radius = 5
    square_side = 6
    
    circle_area = calculate_circle_area(circle_radius)
    square_area = calculate_square_area(square_side)
    
    print(f"Circle area with radius {circle_radius}: {circle_area}")
    print(f"Square area with side length {square_side}: {square_area}")