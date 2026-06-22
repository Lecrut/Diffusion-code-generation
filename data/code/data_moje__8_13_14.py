import math

def calculate_scaled_area(shape, base_dimension, scale_factor):
    if shape == 'rectangle':
        width, height = base_dimension
        return (width * scale_factor) * (height * scale_factor)
    elif shape == 'circle':
        radius = base_dimension
        return math.pi * (radius * scale_factor) ** 2
    else:
        raise ValueError("Unsupported shape")

if __name__ == '__main__':
    rect_result = calculate_scaled_area('rectangle', (2, 3), 1.5)
    circle_result = calculate_scaled_area('circle', 5, 0.5)
    print(rect_result)
    print(circle_result)