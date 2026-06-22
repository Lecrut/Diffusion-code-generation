import math

def validate_dimensions(shape_type, dimensions):
    if shape_type == 'rectangle':
        if len(dimensions) != 2:
            raise ValueError("Rectangle requires exactly two dimensions: length and width.")
        length, width = dimensions
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
    elif shape_type == 'circle':
        if len(dimensions) != 1:
            raise ValueError("Circle requires exactly one dimension: radius.")
        radius = dimensions[0]
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
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
    rectangle_area = calculate_area('rectangle', (9, 4))
    circle_area = calculate_area('circle', (6,))
    print(rectangle_area)
    print(circle_area)