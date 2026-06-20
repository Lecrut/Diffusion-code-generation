def scale_areas(shapes, factor):
    return [{**shape, 'area': shape['width'] * shape['height'] * factor} for shape in shapes]

if __name__ == '__main__':
    sample_shapes = [
        {'name': 'rect1', 'width': 10, 'height': 5},
        {'name': 'rect2', 'width': 4, 'height': 8},
        {'name': 'rect3', 'width': 2, 'height': 3}
    ]
    result = scale_areas(sample_shapes, 2)
    print(result)