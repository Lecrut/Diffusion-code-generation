import math

def area_calculator(shape_type, dimensions):
    if shape_type == 'square':
        side_length = dimensions['side']
        return side_length * side_length
    elif shape_type == 'rectangle':
        length = dimensions['length']
        width = dimensions['width']
        return length * width
    elif shape_type == 'circle':
        radius = dimensions['radius']
        return math.pi * radius * radius
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    square_dimensions = {'side': 5}
    rectangle_dimensions = {'length': 6, 'width': 4}
    circle_dimensions = {'radius': 3}

    square_area = area_calculator('square', square_dimensions)
    rectangle_area = area_calculator('rectangle', rectangle_dimensions)
    circle_area = area_calculator('circle', circle_dimensions)

    print(f"Square Area: {square_area}")
    print(f"Rectangle Area: {rectangle_area}")
    print(f"Circle Area: {circle_area}")