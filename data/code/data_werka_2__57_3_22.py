import math

def area_calculator(shape_type, dimensions):
    if shape_type == 'square':
        side = dimensions.get('side')
        return calculate_square_area(side)
    elif shape_type == 'rectangle':
        length = dimensions.get('length')
        width = dimensions.get('width')
        return calculate_rectangle_area(length, width)
    elif shape_type == 'circle':
        radius = dimensions.get('radius')
        return calculate_circle_area(radius)
    else:
        raise ValueError("Unsupported shape type")

def calculate_square_area(side):
    if side is None or side <= 0:
        raise ValueError("Invalid side length for square")
    return side * side

def calculate_rectangle_area(length, width):
    if length is None or width is None or length <= 0 or width <= 0:
        raise ValueError("Invalid dimensions for rectangle")
    return length * width

def calculate_circle_area(radius):
    if radius is None or radius <= 0:
        raise ValueError("Invalid radius for circle")
    return math.pi * radius * radius

if __name__ == '__main__':
    square_area = area_calculator('square', {'side': 6})
    rectangle_area = area_calculator('rectangle', {'length': 7, 'width': 2})
    circle_area = area_calculator('circle', {'radius': 4})

    print(f"Square Area: {square_area}")
    print(f"Rectangle Area: {rectangle_area}")
    print(f"Circle Area: {circle_area}")