import math

def calculate_circle_circumference(radius):
    return 2 * math.pi * radius

def calculate_square_perimeter(side_length):
    return 4 * side_length

def calculate_shapes(radius, side_length):
    return (calculate_circle_circumference(radius), calculate_square_perimeter(side_length))

if __name__ == '__main__':
    circle_radius = 3.0
    square_side = 6.0
    results = calculate_shapes(circle_radius, square_side)
    print(results)