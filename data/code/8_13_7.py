import math

SCALE_FACTOR = 2

def calculate_area(shape, dimensions):
    if shape == 'rectangle':
        width, height = dimensions
        return width * height
    elif shape == 'circle':
        radius = dimensions
        return math.pi * radius ** 2
    else:
        raise ValueError("Unsupported shape")

def scaled_area(shape, dimensions, scale):
    original_area = calculate_area(shape, dimensions)
    return original_area * (scale ** 2)

if __name__ == '__main__':
    rect_result = scaled_area('rectangle', (10, 5), SCALE_FACTOR)
    circle_result = scaled_area('circle', (10), SCALE_FACTOR)
    print(rect_result)
    print(circle_result)