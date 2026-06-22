import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_rectangle_area(length, width):
    return length * width

if __name__ == '__main__':
    circle_radius = 3
    rectangle_length = 8
    rectangle_width = 4
    
    circle_area = calculate_circle_area(circle_radius)
    rectangle_area = calculate_rectangle_area(rectangle_length, rectangle_width)
    
    if circle_area > rectangle_area:
        print(f"The circle with radius {circle_radius} has a larger area: {circle_area}")
    elif circle_area < rectangle_area:
        print(f"The rectangle with dimensions {rectangle_length}x{rectangle_width} has a larger area: {rectangle_area}")
    else:
        print("Both shapes have the same area.")