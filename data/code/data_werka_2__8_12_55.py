import math

SHAPE_TYPES = {
    'rectangle': lambda width, height: width * height,
    'circle': lambda radius: math.pi * (radius ** 2)
}

def calculate_scaled_area(shape, dimensions, scale_factor):
    if shape not in SHAPE_TYPES:
        raise ValueError("Unsupported shape")
    area_calculator = SHAPE_TYPES[shape]
    area = area_calculator(*dimensions)
    scaled_area = area * scale_factor
    return scaled_area

if __name__ == '__main__':
    rectangle_dimensions = (8, 12)
    circle_dimensions = (6,)
    scale_factor = 1.5
    rectangle_scaled_area = calculate_scaled_area('rectangle', rectangle_dimensions, scale_factor)
    circle_scaled_area = calculate_scaled_area('circle', circle_dimensions, scale_factor)
    print(rectangle_scaled_area)
    print(circle_scaled_area)