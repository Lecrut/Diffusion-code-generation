import math

def calculate_scaled_area(shape_type, dimension, scale_factor):
    if shape_type == 'rectangle':
        length, width = dimension
        scaled_length = length * scale_factor
        scaled_width = width * scale_factor
        return scaled_length * scaled_width
    elif shape_type == 'circle':
        radius = dimension
        scaled_radius = radius * scale_factor
        return math.pi * (scaled_radius ** 2)
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")

if __name__ == '__main__':
    rect_area = calculate_scaled_area('rectangle', (10, 5), 2)
    print(rect_area)
    
    circle_area = calculate_scaled_area('circle', 7, 1.5)
    print(circle_area)