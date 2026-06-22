def calculate_area(shape_type, dimensions):
    if shape_type == 'rectangle':
        length, width = dimensions
        return length * width
    elif shape_type == 'circle':
        radius = dimensions[0]
        return 3.14159 * radius * radius
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
        shape_type = parts[0].strip()
        dimensions = list(map(float, parts[1:]))
        total_area += calculate_area(shape_type, dimensions)
    return total_area

if __name__ == '__main__':
    sample_file_content = """
rectangle, 5.0, 3.0
circle, 2.0
triangle, 4.0, 6.0
"""
    print(total_area_from_file(sample_file_content))