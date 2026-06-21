def scale_areas(shapes, scale_factor):
    if not isinstance(shapes, list) or not all(isinstance(shape, dict) and 'width' in shape and 'height' in shape for shape in shapes):
        raise ValueError("Invalid input: shapes must be a list of dictionaries with 'width' and 'height' keys.")
    if not isinstance(scale_factor, (int, float)) or scale_factor <= 0:
        raise ValueError("Invalid input: scale_factor must be a positive number.")
    
    return [shape['width'] * shape['height'] * scale_factor for shape in shapes]

if __name__ == '__main__':
    try:
        shapes = [
            {'width': 3, 'height': 4},
            {'width': 5, 'height': 6},
            {'width': 7, 'height': 8}
        ]
        scale_factor = 2
        scaled_areas = scale_areas(shapes, scale_factor)
        print(scaled_areas)
    except ValueError as e:
        print(e)