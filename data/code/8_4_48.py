import math

def calculate_area(shape_type, dimensions):
    if shape_type == 'rectangle':
        length, width = dimensions
        area = length * width
    elif shape_type == 'circle':
        radius = dimensions[0]
        area = math.pi * radius * radius
    else:
        raise ValueError("Unsupported shape type")
    return area

if __name__ == '__main__':
    rectangle_length = 10
    rectangle_width = 4
    circle_radius = 6
    
    rectangle_dimensions = (rectangle_length, rectangle_width)
    circle_dimensions = (circle_radius,)
    
    rectangle_area = calculate_area('rectangle', rectangle_dimensions)
    circle_area = calculate_area('circle', circle_dimensions)
    
    print(rectangle_area)
    print(circle_area)