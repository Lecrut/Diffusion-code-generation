import math

def calculate_scaled_area(shape, dimensions, scale_factor):
    if shape == 'rectangle':
        width, height = dimensions
        scaled_width = width * scale_factor
        scaled_height = height * scale_factor
        return scaled_width * scaled_height
    elif shape == 'circle':
        radius = dimensions
        scaled_radius = radius * scale_factor
        return math.pi * (scaled_radius ** 2)
    else:
        raise ValueError("Unsupported shape")

if __name__ == '__main__':
    rectangle_area = calculate_scaled_area('rectangle', (10, 5), 2)
    print(rectangle_area)
    circle_area = calculate_scaled_area('circle', (4), 3)
    print(circle_area)