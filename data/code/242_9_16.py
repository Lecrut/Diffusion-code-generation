import math

def validate_radius(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")

def semicircle_area(radius):
    validate_radius(radius)
    return 0.5 * math.pi * radius ** 2

def validate_dimensions(width, height):
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative")

def rectangle_area(width, height):
    validate_dimensions(width, height)
    return width * height

if __name__ == '__main__':
    semicircle_radius = 4
    rectangle_width = 6
    rectangle_height = 3
    try:
        semicircle_a = semicircle_area(semicircle_radius)
        rectangle_a = rectangle_area(rectangle_width, rectangle_height)
        print(f"Semicircle area: {semicircle_a:.10f}")
        print(f"Rectangle area: {rectangle_a:.10f}")
    except ValueError as e:
        print(e)