def scale_areas(shapes, factor=1.0):
    return [shape['width'] * shape['height'] * factor for shape in shapes]

if __name__ == '__main__':
    sample_shapes = [
        {'width': 3, 'height': 4},
        {'width': 5, 'height': 6},
        {'width': 2, 'height': 2}
    ]
    print(scale_areas(sample_shapes, 2.0))