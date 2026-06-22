def calculate_scaled_area(shape, scale_factor):
    area = shape['width'] * shape['height']
    return area * scale_factor

def scale_areas(shapes, scale_factor):
    return [calculate_scaled_area(shape, scale_factor) for shape in shapes]

if __name__ == '__main__':
    sample_shapes = [
        {'width': 10, 'height': 20},
        {'width': 15, 'height': 25},
        {'width': 20, 'height': 30}
    ]
    scaling_factor = 1.5
    result = scale_areas(sample_shapes, scaling_factor)
    print(result)