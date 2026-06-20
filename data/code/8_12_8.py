def scale_shapes_area(shapes, scale_factor=1.0):
    return [
        {'width': shape['width'], 'height': shape['height'], 'scaled_area': shape['width'] * shape['height'] * (scale_factor ** 2)}
        for shape in shapes
    ]

if __name__ == '__main__':
    sample_shapes = [
        {'width': 3, 'height': 4},
        {'width': 5, 'height': 10},
        {'width': 2, 'height': 2}
    ]
    print(scale_shapes_area(sample_shapes, scale_factor=2.0))