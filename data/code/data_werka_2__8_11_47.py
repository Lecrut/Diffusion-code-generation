def scale_areas(shapes, scale_factor):
    shape_ops = {'area': lambda w, h: w * h}
    return [shape_ops['area'](shape['width'], shape['height']) * scale_factor for shape in shapes]

if __name__ == '__main__':
    sample_shapes = [
        {'width': 2, 'height': 3},
        {'width': 4, 'height': 5},
        {'width': 6, 'height': 7}
    ]
    scaling_factor = 1.5
    result_scaled_areas = scale_areas(sample_shapes, scaling_factor)
    print(result_scaled_areas)