def calculate_scaled_areas(shapes, scale):
    return [width * height * scale for shape in shapes for width, height in [(shape['width'], shape['height'])]]

if __name__ == '__main__':
    sample_shapes = [
        {'width': 2, 'height': 3},
        {'width': 4, 'height': 5},
        {'width': 6, 'height': 7}
    ]
    scale_factor = 3
    scaled_areas = calculate_scaled_areas(sample_shapes, scale_factor)
    print(scaled_areas)