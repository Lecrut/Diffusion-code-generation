import math
CIRCLE_AREA_CONSTANT = 3.14159

def calculate_circle_area(radius):
    return CIRCLE_AREA_CONSTANT * radius ** 2

def calculate_square_area(side_length):
    return side_length ** 2

def sum_of_areas(circle_radius, square_side_length):
    circle_area = calculate_circle_area(circle_radius)
    square_area = calculate_square_area(square_side_length)
    return circle_area + square_area
if __name__ == '__main__':
    total_area = sum_of_areas(3, 4)
    print(total_area)