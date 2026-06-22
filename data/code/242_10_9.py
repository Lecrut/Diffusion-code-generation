import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * radius ** 2

def calculate_rectangle_area(length, width):
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    return length * width

if __name__ == '__main__':
    try:
        circle_radius = 5
        rectangle_length = 10
        rectangle_width = 7
        
        circle_area = calculate_circle_area(circle_radius)
        rectangle_area = calculate_rectangle_area(rectangle_length, rectangle_width)
        
        if circle_area > rectangle_area:
            print(f"The circle with radius {circle_radius} has a larger area: {circle_area}")
        elif circle_area < rectangle_area:
            print(f"The rectangle with length {rectangle_length} and width {rectangle_width} has a larger area: {rectangle_area}")
        else:
            print("Both shapes have the same area.")
    except ValueError as e:
        print(e)