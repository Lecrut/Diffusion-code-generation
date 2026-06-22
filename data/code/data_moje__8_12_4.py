def scale_shapes(shapes, scale_factor):
    return [{'width': s['width'] * scale_factor, 'height': s['height'] * scale_factor, 'area': (s['width'] * s['height']) * (scale_factor ** 2)} for s in shapes]

if __name__ == '__main__':
    sample_shapes = [{'width': 2, 'height': 3}, {'width': 4, 'height': 5}, {'width': 1, 'height': 1}]
    result = scale_shapes(sample_shapes, 2)
    print(result)