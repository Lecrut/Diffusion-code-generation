def calculate_area(base, height):
    shape_types = {
        'triangle': 0.5,
        'rectangle': 1.0
    }
    default_shape = 'triangle'
    multiplier = shape_types.get('triangle', shape_types[default_shape])
    return multiplier * base * height

if __name__ == '__main__':
    sample_base = 7.5
    sample_height = 4.0
    area_result = calculate_area(sample_base, sample_height)
    print(area_result)