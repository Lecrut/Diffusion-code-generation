import math

def calculate_area(shape_type, dimensions):
    if shape_type.lower() == 'circle':
        return _calculate_circle_area(dimensions)
    elif shape_type.lower() == 'rectangle':
        return _calculate_rectangle_area(dimensions)
    else:
        raise ValueError('Unsupported shape type')

def _calculate_circle_area(dimensions):
    radius = dimensions[0]
    area = math.pi * radius ** 2
    return area

def _calculate_rectangle_area(dimensions):
    length, width = dimensions
    area = length * width
    return area
if __name__ == '__main__':
    shape1 = 'circle'
    dimensions1 = [5]
    shape2 = 'rectangle'
    dimensions2 = [4, 6]
    area_circle = calculate_area(shape1, dimensions1)
    area_rectangle = calculate_area(shape2, dimensions2)
    print(f'Area of {shape1} with radius {dimensions1[0]}: {area_circle}')
    print(f'Area of {shape2} with length {dimensions2[0]} and width {dimensions2[1]}: {area_rectangle}')