import math

def validate_dimensions(shape_type, dimensions):
    if shape_type == 'rectangle':
        if len(dimensions) != 2:
            raise ValueError("Rectangle requires exactly two dimensions: length and width.")
    elif shape_type == 'circle':
        if len(dimensions) != 1:
            raise ValueError("Circle requires exactly one dimension: radius.")
    else:
        raise ValueError("Unsupported shape type")

def calculate_area(shape_type, dimensions):
    validate_dimensions(shape_type, dimensions)
    
    if shape_type == 'rectangle':
        length, width = dimensions
        return length * width
    elif shape_type == 'circle':
        radius = dimensions[0]
        return math.pi * radius * radius

if __name__ == '__main__':
    rectangle_area = calculate_area('rectangle', (10, 5))
    circle_area = calculate_area('circle', (3,))
    print(rectangle_area)
    print(circle_area)