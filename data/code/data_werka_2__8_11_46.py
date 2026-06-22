def validate_shapes(shapes):
    if not isinstance(shapes, list) or not all(isinstance(s, dict) and 'width' in s and 'height' in s for s in shapes):
        raise ValueError("Invalid input: shapes must be a list of dictionaries with 'width' and 'height' keys.")

def calculate_area(shape):
    return shape['width'] * shape['height']

def scale_areas(shapes, scale_factor):
    validate_shapes(shapes)
    if not isinstance(scale_factor, (int, float)) or scale_factor <= 0:
        raise ValueError("Invalid input: scale_factor must be a positive number.")
    
    return [calculate_area(shape) * scale_factor for shape in shapes]

if __name__ == '__main__':
    shapes = [
        {'width': 3, 'height': 4},
        {'width': 5, 'height': 6},
        {'width': 7, 'height': 8}
    ]
    scale_factor = 2
    scaled_areas = scale_areas(shapes, scale_factor)
    print(scaled_areas)