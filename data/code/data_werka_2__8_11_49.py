def validate_shapes(shapes):
    if not isinstance(shapes, list):
        raise ValueError("Shapes must be provided as a list.")
    for shape in shapes:
        if not isinstance(shape, dict) or 'width' not in shape or 'height' not in shape:
            raise ValueError("Each shape must be a dictionary with 'width' and 'height' keys.")

def calculate_area(width, height):
    return width * height

def scale_areas(shapes, scale_factor):
    validate_shapes(shapes)
    if not isinstance(scale_factor, (int, float)) or scale_factor <= 0:
        raise ValueError("Scale factor must be a positive number.")
    
    return [calculate_area(shape['width'], shape['height']) * scale_factor for shape in shapes]

if __name__ == '__main__':
    shapes = [
        {'width': 2, 'height': 3},
        {'width': 4, 'height': 5},
        {'width': 6, 'height': 7}
    ]
    scale_factor = 1.5
    scaled_areas = scale_areas(shapes, scale_factor)
    print(scaled_areas)