import math

def validate_positive_number(value):
    if value <= 0:
        raise ValueError("Value must be positive")

def calculate_circle_area(radius):
    validate_positive_number(radius)
    return math.pi * radius ** 2

def calculate_triangle_area(base, height):
    validate_positive_number(base)
    validate_positive_number(height)
    return 0.5 * base * height

if __name__ == '__main__':
    shape = 'triangle'
    if shape == 'circle':
        radius = 8
        area = calculate_circle_area(radius)
        print(area)
    elif shape == 'triangle':
        base = 12
        height = 6
        area = calculate_triangle_area(base, height)
        print(area)