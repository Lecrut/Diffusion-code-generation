import math

def calculate_area_circle(radius):
    return math.pi * radius ** 2

def calculate_area_square(side_length):
    return side_length ** 2

if __name__ == '__main__':
    circle_radius = 5
    square_side_length = 4
    
    circle_area = calculate_area_circle(circle_radius)
    square_area = calculate_area_square(square_side_length)
    
    total_area = circle_area + square_area
    print(total_area)