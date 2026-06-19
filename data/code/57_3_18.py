import math

def validate_dimensions(dimensions):
    if not dimensions:
        raise ValueError("Dimensions cannot be empty")
    if any(d <= 0 for d in dimensions):
        raise ValueError("All dimensions must be positive numbers")

def area_calculator(shape_type, dimensions):
    if shape_type == 'square':
        validate_dimensions(dimensions)
        side_length = dimensions[0]
        return side_length ** 2
    elif shape_type == 'rectangle':
        validate_dimensions(dimensions)
        length, width = dimensions
        return length * width
    elif shape_type == 'circle':
        validate_dimensions(dimensions)
        radius = dimensions[0]
        return math.pi * (radius ** 2)
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    square_area = area_calculator('square', [5])
    rectangle_area = area_calculator('rectangle', [4, 6])
    circle_area = area_calculator('circle', [3])

    print(square_area)
    print(rectangle_area)
    print(circle_area)