import math

def compute_circle_area(radius):
    return math.pi * radius ** 2

def compute_triangle_area(base, height):
    return 0.5 * base * height

if __name__ == '__main__':
    shape = 'triangle'
    if shape == 'circle':
        radius_value = 3
        circle_area_result = compute_circle_area(radius_value)
        print(circle_area_result)
    elif shape == 'triangle':
        base_length = 6
        height_length = 2
        triangle_area_result = compute_triangle_area(base_length, height_length)
        print(triangle_area_result)