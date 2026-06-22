import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

def calculate_triangle_area(base, height):
    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative")
    return 0.5 * base * height

if __name__ == '__main__':
    try:
        shape = 'circle'
        radius = 3
        if shape == 'circle':
            area = calculate_circle_area(radius)
            print(area)
        elif shape == 'triangle':
            base = 6
            height = 2
            area = calculate_triangle_area(base, height)
            print(area)
    except ValueError as e:
        print(e)