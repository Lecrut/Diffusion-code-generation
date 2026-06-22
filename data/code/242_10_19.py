import math

def calculate_area_circle(radius):
    return math.pi * radius ** 2

def calculate_area_rectangle(length, width):
    return length * width

if __name__ == '__main__':
    circle_radius = 5
    rectangle_length = 4
    rectangle_width = 6
    
    area_circle = calculate_area_circle(circle_radius)
    area_rectangle = calculate_area_rectangle(rectangle_length, rectangle_width)
    
    if area_circle > area_rectangle:
        print(f"The circle has a larger area: {area_circle}")
    elif area_circle < area_rectangle:
        print(f"The rectangle has a larger area: {area_rectangle}")
    else:
        print("Both shapes have the same area")