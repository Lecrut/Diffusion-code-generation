import math

def calculate_rectangle_area(length, width):
    return length * width

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_area(shape, *args):
    if shape == 'rectangle':
        length, width = args
        return calculate_rectangle_area(length, width)
    elif shape == 'circle':
        radius = args[0]
        return calculate_circle_area(radius)
    elif shape == 'triangle':
        base, height = args
        return calculate_triangle_area(base, height)
    else:
        raise ValueError("Unsupported shape")

if __name__ == '__main__':
    rectangle_length = 6.0
    rectangle_width = 4.0
    circle_radius = 3.5
    triangle_base = 8.0
    triangle_height = 3.0

    rectangle_area = calculate_area('rectangle', rectangle_length, rectangle_width)
    circle_area = calculate_area('circle', circle_radius)
    triangle_area = calculate_area('triangle', triangle_base, triangle_height)

    print(f"Rectangle area: {rectangle_area}")
    print(f"Circle area: {circle_area}")
    print(f"Triangle area: {triangle_area}")