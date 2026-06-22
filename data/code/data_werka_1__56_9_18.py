import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_circle_perimeter(radius):
    return 2 * math.pi * radius

def calculate_rectangle_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width

def calculate_rectangle_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return 2 * (length + width)

if __name__ == '__main__':
    circle_radius = 7
    rectangle_length = 10
    rectangle_width = 4

    try:
        circle_area = calculate_circle_area(circle_radius)
        circle_perimeter = calculate_circle_perimeter(circle_radius)
        rectangle_area = calculate_rectangle_area(rectangle_length, rectangle_width)
        rectangle_perimeter = calculate_rectangle_perimeter(rectangle_length, rectangle_width)

        print(f"Circle - Radius: {circle_radius}")
        print(f"  Area: {circle_area:.2f}")
        print(f"  Perimeter: {circle_perimeter:.2f}")

        print(f"\nRectangle - Length: {rectangle_length}, Width: {rectangle_width}")
        print(f"  Area: {rectangle_area:.2f}")
        print(f"  Perimeter: {rectangle_perimeter:.2f}")

    except ValueError as e:
        print(e)