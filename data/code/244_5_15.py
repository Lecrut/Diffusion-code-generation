import math
SEMICIRCLE_RADIUS = 4
RECTANGLE_LENGTH = 5
RECTANGLE_WIDTH = 8

def calculate_semicircle_area(radius):
    return 0.5 * math.pi * radius ** 2

def calculate_rectangle_area(length, width):
    return length * width
if __name__ == '__main__':
    semicircle_area = calculate_semicircle_area(SEMICIRCLE_RADIUS)
    rectangle_area = calculate_rectangle_area(RECTANGLE_LENGTH, RECTANGLE_WIDTH)
    total_area = semicircle_area + rectangle_area
    print(total_area)