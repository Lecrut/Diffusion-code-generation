import math

def calculate_rectangle_area(length, width):
    return length * width

def calculate_circle_area(radius):
    return math.pi * radius * radius

def calculate_area(shape_type, dimensions):
    if shape_type == 'rectangle':
        length, width = dimensions
        return calculate_rectangle_area(length, width)
    elif shape_type == 'circle':
        radius = dimensions[0]
        return calculate_circle_area(radius)
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    rectangle_dimensions = (10, 5)
    circle_dimensions = (6,)
    
    rectangle_area = calculate_area('rectangle', rectangle_dimensions)
    circle_area = calculate_area('circle', circle_dimensions)
    
    print(rectangle_area)
    print(circle_area)