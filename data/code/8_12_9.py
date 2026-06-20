def scale_areas(shapes, scale_factor):
    return [
        {**shape, 'area': shape['width'] * shape['height'] * (scale_factor ** 2)}
        for shape in shapes
        if 'width' in shape and 'height' in shape
    ]

if __name__ == '__main__':
    sample_shapes = [
        {'name': 'rect1', 'width': 10, 'height': 5},
        {'name': 'rect2', 'width': 4, 'height': 6},
        {'name': 'rect3', 'width': 0, 'height': 0}
    ]
    result = scale_areas(sample_shapes, 2)
    print(result)