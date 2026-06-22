def scale_areas(shapes, factor):
    return [shape['width'] * shape['height'] * factor for shape in shapes]

if __name__ == '__main__':
    shapes = [
        {'width': 3, 'height': 4},
        {'width': 5, 'height': 6},
        {'width': 7, 'height': 8}
    ]
    scaled_areas = scale_areas(shapes, 2)
    print(scaled_areas)