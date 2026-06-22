import math

def calculate_rectangle_diagonal(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers")
    return math.sqrt(length**2 + width**2)

def calculate_circle_radius(diameter):
    if diameter <= 0:
        raise ValueError("Diameter must be a positive number")
    return diameter / 2

if __name__ == '__main__':
    try:
        rectangle_length = 6
        rectangle_width = 8
        circle_diameter = 15
        
        diagonal = calculate_rectangle_diagonal(rectangle_length, rectangle_width)
        radius = calculate_circle_radius(circle_diameter)
        
        if radius != 0:
            ratio = diagonal / radius
            print(ratio)
        else:
            print("Undefined ratio (division by zero)")
    except ValueError as e:
        print(e)