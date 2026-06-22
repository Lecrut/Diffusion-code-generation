def scale_areas(shapes, scale_factor):
    return [{'area': (shape['width'] * shape['height']) * (scale_factor ** 2)} for shape in shapes]

if __name__ == '__main__':
    sample_shapes = [{'width': 10, 'height': 5}, {'width': 2, 'height': 3}, {'width': 7, 'height': 7}]
    result = scale_areas(sample_shapes, 2)
    print(result)