def scale_areas(shapes, scale_factor):
    return [w * h * scale_factor for shape in shapes for w, h in [(shape['width'], shape['height'])]]

if __name__ == '__main__':
    shapes = [
        {'width': 3, 'height': 4},
        {'width': 5, 'height': 6},
        {'width': 7, 'height': 8}
    ]
    scale_factor = 2
    scaled_areas = scale_areas(shapes, scale_factor)
    print(scaled_areas)