import math

def scale_area(shape, dimension, scale_factor):
    if shape == 'rectangle':
        width, height = dimension
        scaled_width = width * scale_factor
        scaled_height = height * scale_factor
        return scaled_width * scaled_height
    elif shape == 'circle':
        radius = dimension
        scaled_radius = radius * scale_factor
        return math.pi * scaled_radius ** 2
    else:
        raise ValueError("Unsupported shape")

if __name__ == '__main__':
    rectangle_area = scale_area('rectangle', (5, 10), 2)
    print(rectangle_area)
    circle_area = scale_area('circle', 3, 3)
    print(circle_area)