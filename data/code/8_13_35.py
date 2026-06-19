import math

def calculate_scaled_area(figure, dimensions, scale_factor):
    if figure == 'rectangle':
        length, width = dimensions
        area = length * width
    elif figure == 'circle':
        radius = dimensions[0]
        area = math.pi * (radius ** 2)
    else:
        raise ValueError("Unsupported figure type")
    
    scaled_area = area * scale_factor
    return scaled_area

if __name__ == '__main__':
    rectangle_dimensions = (5, 3)
    circle_dimensions = (4,)
    scale_factor = 2.0
    
    rectangle_scaled_area = calculate_scaled_area('rectangle', rectangle_dimensions, scale_factor)
    circle_scaled_area = calculate_scaled_area('circle', circle_dimensions, scale_factor)
    
    print(rectangle_scaled_area)
    print(circle_scaled_area)