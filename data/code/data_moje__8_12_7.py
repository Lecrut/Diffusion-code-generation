def scale_shape_areas(shapes, scale_factor):
    return [{'width': s['width'], 'height': s['height'], 'area': s['width'] * s['height'] * (scale_factor ** 2)} for s in shapes]

if __name__ == '__main__':
    sample_shapes = [{'width': 10, 'height': 5}, {'width': 4, 'height': 8}, {'width': 6, 'height': 6}]
    result = scale_shape_areas(sample_shapes, 2)
    print(result)