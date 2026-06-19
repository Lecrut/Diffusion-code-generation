import math

def area_calculator(shape_type, dimensions):
    if shape_type == 'square':
        side_length = dimensions.get('side')
        if not isinstance(side_length, (int, float)) or side_length <= 0:
            raise ValueError("Invalid side length for square")
        return side_length ** 2
    elif shape_type == 'rectangle':
        width = dimensions.get('width')
        height = dimensions.get('height')
        if not all(isinstance(x, (int, float)) and x > 0 for x in [width, height]):
            raise ValueError("Invalid dimensions for rectangle")
        return width * height
    elif shape_type == 'circle':
        radius = dimensions.get('radius')
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Invalid radius for circle")
        return math.pi * radius ** 2
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    square_area = area_calculator('square', {'side': 5})
    rectangle_area = area_calculator('rectangle', {'width': 4, 'height': 6})
    circle_area = area_calculator('circle', {'radius': 3})

    print("Square Area:", square_area)
    print("Rectangle Area:", rectangle_area)
    print("Circle Area:", circle_area)