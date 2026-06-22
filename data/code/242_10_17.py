import math

CIRCLE_RADIUS = 5
RECTANGLE_LENGTH = 10
RECTANGLE_WIDTH = 7

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_rectangle_area(length, width):
    return length * width

def compare_areas(circle_radius=CIRCLE_RADIUS, rectangle_length=RECTANGLE_LENGTH, rectangle_width=RECTANGLE_WIDTH):
    circle_area = calculate_circle_area(circle_radius)
    rectangle_area = calculate_rectangle_area(rectangle_length, rectangle_width)
    
    if circle_area > rectangle_area:
        print(f"The circle with radius {circle_radius} has a larger area: {circle_area}")
    elif circle_area < rectangle_area:
        print(f"The rectangle with dimensions {rectangle_length}x{rectangle_width} has a larger area: {rectangle_area}")
    else:
        print("Both shapes have the same area.")

if __name__ == '__main__':
    compare_areas()