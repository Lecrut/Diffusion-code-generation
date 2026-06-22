import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_circle_perimeter(radius):
    return 2 * math.pi * radius

def calculate_rectangle_area(length, width):
    return length * width

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    circle_radius = 5
    rectangle_length = 4
    rectangle_width = 6

    circle_area = calculate_circle_area(circle_radius)
    circle_perimeter = calculate_circle_perimeter(circle_radius)
    rectangle_area = calculate_rectangle_area(rectangle_length, rectangle_width)
    rectangle_perimeter = calculate_rectangle_perimeter(rectangle_length, rectangle_width)

    print(f"Circle Area: {circle_area}")
    print(f"Circle Perimeter: {circle_perimeter}")
    print(f"Rectangle Area: {rectangle_area}")
    print(f"Rectangle Perimeter: {rectangle_perimeter}")