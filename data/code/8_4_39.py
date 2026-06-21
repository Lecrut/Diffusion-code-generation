import math

def calculate_area(shape_type, dimensions):
    if shape_type == 'rectangle':
        length, width = dimensions
        return length * width
    elif shape_type == 'circle':
        radius = dimensions[0]
        return math.pi * radius * radius
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    rectangle_dimensions = (8, 4)
    circle_dimensions = (5,)
    
    rectangle_area = calculate_area('rectangle', rectangle_dimensions)
    circle_area = calculate_area('circle', circle_dimensions)
    
    print(rectangle_area)
    print(circle_area)