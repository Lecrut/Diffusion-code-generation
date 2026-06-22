def scale_areas(shapes, scale_factor):
    return [shape['width'] * shape['height'] * scale_factor for shape in shapes]

if __name__ == '__main__':
    shapes = [
        {'width': 3, 'height': 4},
        {'width': 5, 'height': 6},
        {'width': 2, 'height': 7}
    ]
    scale_factor = 2.5
    result = scale_areas(shapes, scale_factor)
    print(result)