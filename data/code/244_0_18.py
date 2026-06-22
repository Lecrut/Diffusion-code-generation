import math
CIRCLE_RADIUS = 5
SQUARE_SIDE_LENGTH = 4

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_square_area(side_length):
    return side_length ** 2

def calculate_total_area():
    circle_area = calculate_circle_area(CIRCLE_RADIUS)
    square_area = calculate_square_area(SQUARE_SIDE_LENGTH)
    total_area = circle_area + square_area
    return total_area
if __name__ == '__main__':
    total_area = calculate_total_area()
    print(total_area)