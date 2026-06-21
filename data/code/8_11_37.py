def scale_areas(shapes, scale_factor):
    if not shapes or scale_factor <= 0:
        return []
    
    def calculate_area(shape):
        return shape['width'] * shape['height']
    
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