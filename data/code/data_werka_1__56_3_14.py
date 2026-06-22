import math

def validate_dimensions(length, width, radius):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")

def calculate_area_rectangle(length, width):
    return length * width

def calculate_area_circle(radius):
    return math.pi * radius ** 2

def compare_areas(length, width, radius):
    validate_dimensions(length, width, radius)
    area_rectangle = calculate_area_rectangle(length, width)
    area_circle = calculate_area_circle(radius)
    print(f"Rectangle Area: {area_rectangle:.2f}")
    print(f"Circle Area: {area_circle:.2f}")

if __name__ == '__main__':
    length = 8.0
    width = 4.5
    radius = 6.2
    compare_areas(length, width, radius)