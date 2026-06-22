import math

def calculate_area(shape, dimensions):
    if shape == 'rectangle':
        width, height = dimensions
        return width * height
    elif shape == 'circle':
        radius = dimensions[0]
        return math.pi * (radius ** 2)
    else:
        raise ValueError("Unsupported shape")

def scaled_area(shape, dimensions, scale_factor):
    area = calculate_area(shape, dimensions)
    return area * scale_factor

if __name__ == '__main__':
    rectangle_dimensions = (5, 10)
    circle_dimensions = (7,)
    scale_factor = 2.5
    rectangle_scaled_area = scaled_area('rectangle', rectangle_dimensions, scale_factor)
    circle_scaled_area = scaled_area('circle', circle_dimensions, scale_factor)
    print(f"Scaled area of the rectangle: {rectangle_scaled_area}")
    print(f"Scaled area of the circle: {circle_scaled_area}")