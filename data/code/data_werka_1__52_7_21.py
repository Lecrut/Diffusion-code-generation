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
    try:
        total_area = 0
        lines = file_content.strip().split('\n')
        for line in lines:
            parts = line.split(',')
            if len(parts) != 2:
                raise ValueError("Invalid line format")
            shape_type, dimensions_str = parts
            dimensions = list(map(float, dimensions_str.split()))
            total_area += calculate_area(shape_type, dimensions)
        return total_area
    except Exception as e:
        print(f"Error processing file: {e}")
        return 0

if __name__ == '__main__':
    sample_file_content = """rectangle,3.0,4.0
circle,5.0
triangle,6.0,8.0"""
    print(total_area_from_file(sample_file_content))