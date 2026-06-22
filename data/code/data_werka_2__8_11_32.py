def scale_areas(shapes, scale_factor):
    return [{'width': s['width'] * scale_factor, 'height': s['height'] * scale_factor} for s in shapes]

if __name__ == '__main__':
    shapes = [
        {'width': 2, 'height': 3},
        {'width': 4, 'height': 5},
        {'width': 6, 'height': 7}
    ]
    scale_factor = 2
    scaled_shapes = scale_areas(shapes, scale_factor)
    print(scaled_shapes)