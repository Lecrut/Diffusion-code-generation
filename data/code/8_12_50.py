import math
SCALE_FACTOR = 2.5
RECTANGLE_DIMENSIONS = (5, 10)
CIRCLE_DIMENSIONS = (7,)

def calculate_rectangle_area(width, height):
    return width * height

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_scaled_area(shape, dimensions, scale_factor):
    if shape == 'rectangle':
        area = calculate_rectangle_area(*dimensions)
    elif shape == 'circle':
        area = calculate_circle_area(dimensions[0])
    else:
        raise ValueError('Unsupported shape')
    scaled_area = area * scale_factor
    return scaled_area
if __name__ == '__main__':
    rectangle_scaled_area = calculate_scaled_area('rectangle', RECTANGLE_DIMENSIONS, SCALE_FACTOR)
    circle_scaled_area = calculate_scaled_area('circle', CIRCLE_DIMENSIONS, SCALE_FACTOR)
    print(f'Scaled area of the rectangle: {rectangle_scaled_area}')
    print(f'Scaled area of the circle: {circle_scaled_area}')