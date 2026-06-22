def scale_areas(shapes, scale_factor):
    area_map = {'area': lambda w, h: w * h}
    return [area_map['area'](shape['width'], shape['height']) * scale_factor for shape in shapes]

if __name__ == '__main__':
    shapes = [
        {'width': 3, 'height': 4},
        {'width': 5, 'height': 6},
        {'width': 7, 'height': 8}
    ]
    scale_factor = 2
    scaled_areas = scale_areas(shapes, scale_factor)
    print(scaled_areas)