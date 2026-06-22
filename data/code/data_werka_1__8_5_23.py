def calculate_area(shape_type, dimensions):
    if shape_type == 'rectangle':
        length, width = dimensions
        return length * width
    elif shape_type == 'circle':
        radius = dimensions[0]
        import math
        return math.pi * (radius ** 2)
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    rectangle_area = calculate_area('rectangle', (5, 3))
    circle_area = calculate_area('circle', (4,))
    print(rectangle_area)
    print(circle_area)