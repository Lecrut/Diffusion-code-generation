import math

def calculate_area(shape_type, dimensions):
    if shape_type.lower() == 'rectangle':
        return _calculate_rectangle_area(dimensions)
    elif shape_type.lower() == 'circle':
        return _calculate_circle_area(dimensions)
    else:
        raise ValueError('Unsupported shape type')

def _calculate_rectangle_area(dimensions):
    try:
        length, width = dimensions
        if length <= 0 or width <= 0:
            raise ValueError('Dimensions must be positive numbers')
        return length * width
    except TypeError:
        raise ValueError('Rectangle requires two dimensions: length and width')

def _calculate_circle_area(dimensions):
    try:
        radius = dimensions[0]
        if radius <= 0:
            raise ValueError('Radius must be a positive number')
        return math.pi * radius ** 2
    except (TypeError, IndexError):
        raise ValueError('Circle requires one dimension: radius')

if __name__ == '__main__':
    rectangle_dimensions = (5, 3)
    circle_dimensions = (4,)
    
    try:
        rectangle_area = calculate_area('rectangle', rectangle_dimensions)
        print(f"Rectangle area: {rectangle_area}")
    except Exception as e:
        print(f"Error calculating rectangle area: {e}")

    try:
        circle_area = calculate_area('circle', circle_dimensions)
        print(f"Circle area: {circle_area}")
    except Exception as e:
        print(f"Error calculating circle area: {e}")