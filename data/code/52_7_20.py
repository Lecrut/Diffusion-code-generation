import math

SHAPE_AREA_FUNCTIONS = {
    'rectangle': lambda length, width: length * width,
    'circle': lambda radius: math.pi * (radius ** 2),
    'triangle': lambda base, height: 0.5 * base * height
}

def calculate_area(shape_type, dimensions):
    if shape_type in SHAPE_AREA_FUNCTIONS:
        return SHAPE_AREA_FUNCTIONS[shape_type](*dimensions)
    else:
        raise ValueError("Unsupported shape type")

def total_area_from_file(file_content):
    total_area = 0
    lines = file_content.strip().split('\n')
    for line in lines:
        parts = line.split(',')
        shape_type = parts[0].strip()
        dimensions = [float(part.strip()) for part in parts[1:]]
        total_area += calculate_area(shape_type, dimensions)
    return total_area

if __name__ == '__main__':
    sample_file_content = """rectangle, 5, 3
circle, 4
triangle, 6, 2"""
    print(total_area_from_file(sample_file_content))