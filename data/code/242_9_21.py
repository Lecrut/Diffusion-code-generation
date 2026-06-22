import math

def semicircle_area(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return 0.5 * math.pi * radius ** 2

def rectangle_area(width, height):
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative")
    return width * height

if __name__ == '__main__':
    semicircle_radius = 4
    rectangle_width = 6
    rectangle_height = 3
    try:
        semicircle_area_value = semicircle_area(semicircle_radius)
        rectangle_area_value = rectangle_area(rectangle_width, rectangle_height)
        print(f"Semicircle area: {semicircle_area_value:.10f}")
        print(f"Rectangle area: {rectangle_area_value:.10f}")
    except ValueError as e:
        print(e)