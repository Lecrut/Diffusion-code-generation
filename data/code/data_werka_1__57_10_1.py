import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_triangle_area(base, height):
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