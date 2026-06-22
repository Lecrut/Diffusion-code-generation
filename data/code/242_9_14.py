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
        semicircle_result = semicircle_area(semicircle_radius)
        rectangle_result = rectangle_area(rectangle_width, rectangle_height)
        
        print(f"Semicircle area: {semicircle_result:.10f}")
        print(f"Rectangle area: {rectangle_result:.10f}")
    except ValueError as e:
        print(e)