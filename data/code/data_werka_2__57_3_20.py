import math

def area_calculator(shape_type, dimensions):
    if shape_type == 'square':
        side_length = dimensions.get('side')
        if side_length is None:
            raise ValueError("Missing dimension: side")
        return side_length ** 2
    elif shape_type == 'rectangle':
        length = dimensions.get('length')
        width = dimensions.get('width')
        if length is None or width is None:
            raise ValueError("Missing dimensions: length and width")
        return length * width
    elif shape_type == 'circle':
        radius = dimensions.get('radius')
        if radius is None:
            raise ValueError("Missing dimension: radius")
        return math.pi * (radius ** 2)
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")

if __name__ == '__main__':
    square_area = area_calculator('square', {'side': 4})
    rectangle_area = area_calculator('rectangle', {'length': 5, 'width': 3})
    circle_area = area_calculator('circle', {'radius': 7})

    print(f"Square Area: {square_area}")
    print(f"Rectangle Area: {rectangle_area}")
    print(f"Circle Area: {circle_area}")