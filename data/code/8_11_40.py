def scale_areas(shapes, scale_factor):
    def calculate_area(shape):
        return shape['width'] * shape['height']
    
    scaled_areas = [calculate_area(shape) * scale_factor for shape in shapes]
    return scaled_areas

if __name__ == '__main__':
    sample_shapes = [
        {'width': 10, 'height': 20},
        {'width': 15, 'height': 25},
        {'width': 20, 'height': 30}
    ]
    scaling_factor = 1.5
    result = scale_areas(sample_shapes, scaling_factor)
    print(result)