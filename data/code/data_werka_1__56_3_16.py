import math

def calculate_area_rectangle(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width

def calculate_area_circle(radius):
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")
    return math.pi * radius ** 2

def compare_areas(length, width, radius):
    try:
        rectangle_area = calculate_area_rectangle(length, width)
        circle_area = calculate_area_circle(radius)
        print(f"Rectangle Area: {rectangle_area:.2f}")
        print(f"Circle Area: {circle_area:.2f}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    length = 8.0
    width = 4.5
    radius = 6.0
    compare_areas(length, width, radius)