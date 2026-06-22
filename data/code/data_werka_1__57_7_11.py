import math

def calculate_area(shape_type, dimensions):
    if shape_type.lower() == 'circle':
        return _calculate_circle_area(dimensions[0])
    elif shape_type.lower() == 'rectangle':
        return _calculate_rectangle_area(dimensions)
    else:
        raise ValueError('Unsupported shape type')

def _calculate_circle_area(radius):
    return math.pi * radius ** 2

def _calculate_rectangle_area(dimensions):
    length, width = dimensions
    return length * width

if __name__ == '__main__':
    circle_radius = 3.0
    rectangle_dimensions = (4.5, 6.0)
    
    circle_area = calculate_area('circle', [circle_radius])
    rectangle_area = calculate_area('rectangle', rectangle_dimensions)
    
    print(f"Circle area with radius {circle_radius}: {circle_area}")
    print(f"Rectangle area with dimensions {rectangle_dimensions}: {rectangle_area}")