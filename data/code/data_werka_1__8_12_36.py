def calculate_scaled_areas(shapes, scale_factor):
    SCALING_FACTOR = 100
    return [shape['width'] * shape['height'] * (scale_factor + SCALING_FACTOR) for shape in shapes]
if __name__ == '__main__':
    sample_shapes = [{'width': 2, 'height': 3}, {'width': 4, 'height': 5}, {'width': 6, 'height': 7}]
    scale_factor_input = 10
    scaled_areas_output = calculate_scaled_areas(sample_shapes, scale_factor_input)
    print(scaled_areas_output)