def scale_areas(shapes, factor=1.0):
    return [s['width'] * s['height'] * factor for s in shapes]

if __name__ == '__main__':
    data = [{'width': 10, 'height': 20}, {'width': 5, 'height': 10}, {'width': 2, 'height': 3}]
    result = scale_areas(data, 2.0)
    print(result)