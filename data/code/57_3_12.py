import math

def area_calculator(shape_type, dimensions):
    if shape_type == 'square':
        side_length = dimensions.get('side')
        return side_length ** 2 if side_length is not None else None
    
    elif shape_type == 'rectangle':
        length = dimensions.get('length')
        width = dimensions.get('width')
        return length * width if length is not None and width is not None else None
    
    elif shape_type == 'circle':
        radius = dimensions.get('radius')
        return math.pi * (radius ** 2) if radius is not None else None
    
    else:
        return None

if __name__ == '__main__':
    square_area = area_calculator('square', {'side': 5})
    rectangle_area = area_calculator('rectangle', {'length': 4, 'width': 3})
    circle_area = area_calculator('circle', {'radius': 2})
    
    print(square_area)
    print(rectangle_area)
    print(circle_area)