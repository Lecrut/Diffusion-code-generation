import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

def calculate_rectangle_area(length, width):
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative")
    return length * width

if __name__ == '__main__':
    circle_radius = 5
    rectangle_length = 10
    rectangle_width = 7
    
    try:
        circle_area_result = calculate_circle_area(circle_radius)
        rectangle_area_result = calculate_rectangle_area(rectangle_length, rectangle_width)
        total_area = circle_area_result + rectangle_area_result
        print(total_area)
    except ValueError as e:
        print(e)