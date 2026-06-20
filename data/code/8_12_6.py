def scale_areas(shapes, scale_factor):
    return [s['width'] * scale_factor * s['height'] * scale_factor for s in shapes]

if __name__ == '__main__':
    sample_shapes = [{'width': 10, 'height': 5}, {'width': 20, 'height': 30}]
    result = scale_areas(sample_shapes, 2)
    print(result)