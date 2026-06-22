import math

SHAPE_AREA_FUNCTIONS = {
    'rectangle': lambda width, height: width * height,
    'circle': lambda radius: math.pi * (radius ** 2)
}

def calculate_scaled_area(shape, dimensions, scale_factor):
    area_function = SHAPE_AREA_FUNCTIONS.get(shape)
    if not area_function:
        raise ValueError("Unsupported shape")
    area = area_function(*dimensions)
    scaled_area = area * scale_factor
    return scaled_area

if __name__ == '__main__':
    rectangle_dimensions = (6, 12)
    circle_dimensions = (8,)
    scale_factor = 3.0
    
    rectangle_scaled_area = calculate_scaled_area('rectangle', rectangle_dimensions, scale_factor)
    circle_scaled_area = calculate_scaled_area('circle', circle_dimensions, scale_factor)
    
    print(f'Scaled area of the rectangle: {rectangle_scaled_area}')
    print(f'Scaled area of the circle: {circle_scaled_area}')