import math

def calculate_scaled_area(shape, dimensions, scale_factor):
    if shape == 'rectangle':
        width, height = dimensions
        area = width * height
    elif shape == 'circle':
        radius = dimensions[0]
        area = math.pi * (radius ** 2)
    else:
        raise ValueError("Unsupported shape")
    
    scaled_area = area * scale_factor
    return scaled_area

if __name__ == '__main__':
    rectangle_dimensions = (5, 10)
    circle_dimensions = (7,)
    scale_factor = 1.5
    
    rectangle_scaled_area = calculate_scaled_area('rectangle', rectangle_dimensions, scale_factor)
    circle_scaled_area = calculate_scaled_area('circle', circle_dimensions, scale_factor)
    
    print(rectangle_scaled_area)
    print(circle_scaled_area)