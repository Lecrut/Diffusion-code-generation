import math

def calculate_rectangle_area(length, width):
    return length * width

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_area(shape, *args):
    if shape == 'rectangle':
        return calculate_rectangle_area(*args)
    elif shape == 'circle':
        return calculate_circle_area(*args)
    elif shape == 'triangle':
        return calculate_triangle_area(*args)
    else:
        raise ValueError("Unsupported shape")

if __name__ == '__main__':
    rectangle_area = calculate_area('rectangle', 6, 9)
    circle_area = calculate_area('circle', 8)
    triangle_area = calculate_area('triangle', 10, 5)
    print(f"Rectangle Area: {rectangle_area}")
    print(f"Circle Area: {circle_area}")
    print(f"Triangle Area: {triangle_area}")