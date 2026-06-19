def scale_areas(shapes, scale_factor):
    return [shape['width'] * shape['height'] * scale_factor for shape in shapes]

if __name__ == '__main__':
    sample_shapes = [
        {'width': 3, 'height': 4},
        {'width': 5, 'height': 6},
        {'width': 7, 'height': 8}
    ]
    scaled_areas = scale_areas(sample_shapes, 2)
    print(scaled_areas)