import math

def area_calculator(shape_type, dimensions):
    if shape_type == 'square':
        side_length = dimensions.get('side')
        return side_length * side_length
    elif shape_type == 'rectangle':
        length = dimensions.get('length')
        width = dimensions.get('width')
        return length * width
    elif shape_type == 'circle':
        radius = dimensions.get('radius')
        return math.pi * radius ** 2
    else:
        raise ValueError('Unsupported shape type')
if __name__ == '__main__':
    square_dimensions = {'side': 5}
    rectangle_dimensions = {'length': 4, 'width': 6}
    circle_dimensions = {'radius': 3}
    print(area_calculator('square', square_dimensions))
    print(area_calculator('rectangle', rectangle_dimensions))
    print(area_calculator('circle', circle_dimensions))