import math

def area_calculator(shape_type, dimensions):
    if shape_type == 'square':
        side = dimensions.get('side')
        if not isinstance(side, (int, float)) or side <= 0:
            raise ValueError("Invalid side length for square")
        return side * side
    elif shape_type == 'rectangle':
        length = dimensions.get('length')
        width = dimensions.get('width')
        if not all(isinstance(x, (int, float)) and x > 0 for x in [length, width]):
            raise ValueError("Invalid dimensions for rectangle")
        return length * width
    elif shape_type == 'circle':
        radius = dimensions.get('radius')
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Invalid radius for circle")
        return math.pi * radius ** 2
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    square_area = area_calculator('square', {'side': 6})
    rectangle_area = area_calculator('rectangle', {'length': 7, 'width': 8})
    circle_area = area_calculator('circle', {'radius': 9})

    print(f"Square Area: {square_area}")
    print(f"Rectangle Area: {rectangle_area}")
    print(f"Circle Area: {circle_area}")