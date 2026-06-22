import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_square_area(side_length):
    return side_length ** 2

def validate_dimensions(circle_radius, square_side_length):
    if circle_radius <= 0 or square_side_length <= 0:
        raise ValueError("Both dimensions must be greater than zero")

if __name__ == '__main__':
    circle_radius = 5
    square_side_length = 4
    
    validate_dimensions(circle_radius, square_side_length)
    
    circle_area = calculate_circle_area(circle_radius)
    square_area = calculate_square_area(square_side_length)
    
    total_area = circle_area + square_area
    
    print(total_area)