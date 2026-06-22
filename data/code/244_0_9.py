import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_square_area(side_length):
    return side_length ** 2

def total_areas(circle_radius, square_side_length):
    circle_area = calculate_circle_area(circle_radius)
    square_area = calculate_square_area(square_side_length)
    return circle_area + square_area

if __name__ == '__main__':
    circle_radius = 5
    square_side_length = 4
    result = total_areas(circle_radius, square_side_length)
    print(result)