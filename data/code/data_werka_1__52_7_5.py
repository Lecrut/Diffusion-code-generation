import math

def calculate_area(shape_type, dimensions):
    if shape_type == 'rectangle':
        length, width = dimensions
        return length * width
    elif shape_type == 'circle':
        radius = dimensions[0]
        return math.pi * (radius ** 2)
    elif shape_type == 'triangle':
        base, height = dimensions
        return 0.5 * base * height
    else:
        raise ValueError("Unsupported shape type")

def total_area_from_file(file_content):
    total_area = 0
    lines = file_content.strip().split('\n')
    for line in lines:
        parts = line.split(',')
        if len(parts) < 2:
            continue
        shape_type = parts[0].strip()
        try:
            dimensions = list(map(float, parts[1:]))
            total_area += calculate_area(shape_type, dimensions)
        except ValueError:
            continue
    return total_area

if __name__ == '__main__':
    sample_file_content = """rectangle, 5, 3
circle, 2
triangle, 4, 6"""
    print(total_area_from_file(sample_file_content))