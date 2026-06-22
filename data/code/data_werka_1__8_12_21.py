def scale_areas(shapes, scale_factor=2):
    return [shape['width'] * shape['height'] * scale_factor for shape in shapes]

if __name__ == '__main__':
    shapes = [{'width': 3, 'height': 4}, {'width': 5, 'height': 6}]
    scaled_areas = scale_areas(shapes)
    print(scaled_areas)