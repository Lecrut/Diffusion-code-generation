import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_circle_perimeter(radius):
    return 2 * math.pi * radius

def calculate_square_area(side_length):
    return side_length ** 2

def calculate_square_perimeter(side_length):
    return 4 * side_length

if __name__ == '__main__':
    circle_radius = 5
    square_side_length = 4
    
    circle_area = calculate_circle_area(circle_radius)
    circle_perimeter = calculate_circle_perimeter(circle_radius)
    
    square_area = calculate_square_area(square_side_length)
    square_perimeter = calculate_square_perimeter(square_side_length)
    
    print(f"Circle Area: {circle_area}")
    print(f"Circle Perimeter: {circle_perimeter}")
    print(f"Square Area: {square_area}")
    print(f"Square Perimeter: {square_perimeter}")