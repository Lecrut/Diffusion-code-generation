import math

def calculate_area_circle(radius):
    return math.pi * radius ** 2

def calculate_area_rectangle(length, width):
    return length * width

if __name__ == '__main__':
    circle_radius = 5
    rectangle_length = 10
    rectangle_width = 7
    
    area_circle = calculate_area_circle(circle_radius)
    area_rectangle = calculate_area_rectangle(rectangle_length, rectangle_width)
    
    if area_circle > area_rectangle:
        print(f"The circle with radius {circle_radius} has a larger area.")
    elif area_circle < area_rectangle:
        print(f"The rectangle with dimensions {rectangle_length}x{rectangle_width} has a larger area.")
    else:
        print("Both shapes have the same area.")