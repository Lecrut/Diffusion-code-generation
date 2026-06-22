def compute_scaled_areas(shapes, scale_factor=1.0):
    return [shape['width'] * shape['height'] * scale_factor for shape in shapes]

if __name__ == '__main__':
    sample_shapes = [
        {'width': 3, 'height': 4},
        {'width': 5, 'height': 6},
        {'width': 2, 'height': 7}
    ]
    print(compute_scaled_areas(sample_shapes, 2.0))