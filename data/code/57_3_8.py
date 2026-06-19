import math

def area_calculator(shape_type, dimensions):
    if shape_type == 'square':
        side_length = dimensions.get('side')
        return side_length ** 2
    elif shape_type == 'rectangle':
        length = dimensions.get('length')
        width = dimensions.get('width')
        return length * width
    elif shape_type == 'circle':
        radius = dimensions.get('radius')
        return math.pi * (radius ** 2)
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    square_area = area_calculator('square', {'side': 4})
    print(f"Area of square: {square_area}")

    rectangle_area = area_calculator('rectangle', {'length': 5, 'width': 3})
    print(f"Area of rectangle: {rectangle_area}")

    circle_area = area_calculator('circle', {'radius': 7})
    print(f"Area of circle: {circle_area}")