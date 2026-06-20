def scale_areas(shapes, scale_factor=1.0):
    return [{'width': s['width'] * scale_factor, 'height': s['height'] * scale_factor, 'area': s['width'] * s['height'] * scale_factor * scale_factor} for s in shapes]

if __name__ == '__main__':
    sample_shapes = [
        {'width': 3, 'height': 4},
        {'width': 5, 'height': 2},
        {'width': 7, 'height': 1}
    ]
    print(scale_areas(sample_shapes, 2.0))