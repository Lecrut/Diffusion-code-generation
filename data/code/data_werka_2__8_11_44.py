def scale_areas(shapes, scale_factor):
    if not all(isinstance(shape, dict) and 'width' in shape and 'height' in shape for shape in shapes):
        raise ValueError("All elements in shapes must be dictionaries with 'width' and 'height' keys.")
    if scale_factor <= 0:
        raise ValueError("Scale factor must be a positive number.")
    
    return [shape['width'] * shape['height'] * scale_factor for shape in shapes]

if __name__ == '__main__':
    shapes = [
        {'width': 3, 'height': 4},
        {'width': 5, 'height': 6},
        {'width': 7, 'height': 8}
    ]
    scale_factor = 2
    try:
        scaled_areas = scale_areas(shapes, scale_factor)
        print(scaled_areas)
    except ValueError as e:
        print(e)