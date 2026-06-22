import math

def validate_positive_number(value):
    if value <= 0:
        raise ValueError("The value must be positive")

def calculate_rectangle_area(length, width):
    validate_positive_number(length)
    validate_positive_number(width)
    return length * width

def calculate_circle_area(radius):
    validate_positive_number(radius)
    return math.pi * (radius ** 2)

def calculate_triangle_area(base, height):
    validate_positive_number(base)
    validate_positive_number(height)
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
    rectangle_area = calculate_area('rectangle', 5, 3)
    circle_area = calculate_area('circle', 4)
    triangle_area = calculate_area('triangle', 6, 2)
    print(f"Rectangle area: {rectangle_area}")
    print(f"Circle area: {circle_area}")
    print(f"Triangle area: {triangle_area}")