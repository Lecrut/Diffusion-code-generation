def scale_areas(shapes, scale_factor):
    return [{'width': s['width'] * scale_factor, 'height': s['height'] * scale_factor, 'area': (s['width'] * s['height']) * (scale_factor ** 2)} for s in shapes]

if __name__ == '__main__':
    shapes = [
        {'width': 3, 'height': 4},
        {'width': 5, 'height': 6}
    ]
    scale_factor = 2
    scaled_shapes = scale_areas(shapes, scale_factor)
    print(scaled_shapes)