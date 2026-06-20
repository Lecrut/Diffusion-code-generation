def scale_areas(shapes, scale_factor):
    return [s['width'] * s['height'] * (scale_factor ** 2) for s in shapes]

if __name__ == '__main__':
    shapes = [{'width': 2, 'height': 3}, {'width': 5, 'height': 4}, {'width': 1, 'height': 1}]
    print(scale_areas(shapes, 2))