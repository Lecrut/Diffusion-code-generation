import math

def validate_radius(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")

def validate_base_and_height(base, height):
    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative")

def calculate_circle_area(radius):
    validate_radius(radius)
    return math.pi * radius ** 2

def calculate_triangle_area(base, height):
    validate_base_and_height(base, height)
    return 0.5 * base * height

if __name__ == '__main__':
    shape = 'circle'
    if shape == 'circle':
        radius = 5
        area = calculate_circle_area(radius)
        print(area)
    elif shape == 'triangle':
        base = 10
        height = 4
        area = calculate_triangle_area(base, height)
        print(area)