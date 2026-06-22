import math

def calculate_area(shape_type, dimensions):
    if shape_type == 'rectangle':
        length, width = dimensions
        return validate_dimensions(length, width) * validate_dimensions(width)
    elif shape_type == 'circle':
        radius = dimensions[0]
        return validate_radius(radius) * math.pi * (validate_radius(radius) ** 2)
    elif shape_type == 'triangle':
        base, height = dimensions
        return 0.5 * validate_dimensions(base) * validate_dimensions(height)
    else:
        raise ValueError("Unsupported shape type")

def validate_dimensions(dimension):
    if not isinstance(dimension, (int, float)) or dimension <= 0:
        raise ValueError("Dimension must be a positive number")
    return dimension

def validate_radius(radius):
    if not isinstance(radius, (int, float)) or radius < 0:
        raise ValueError("Radius must be a non-negative number")
    return radius

def total_area_from_file(file_content):
    total_area = 0
    lines = file_content.strip().split('\n')
    for line in lines:
        parts = line.split(',')
        if len(parts) != 2:
            raise ValueError("Each line must contain exactly two elements: shape_type and dimensions")
        shape_type, dim_str = parts
        try:
            dimensions = list(map(float, dim_str.strip('[]').split()))
        except ValueError:
            raise ValueError("Dimensions must be a list of numbers")
        total_area += calculate_area(shape_type, dimensions)
    return total_area

if __name__ == '__main__':
    sample_file_content = """rectangle,[3,4]
circle,[5]
triangle,[6,7]"""
    print(total_area_from_file(sample_file_content))