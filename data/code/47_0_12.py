def calculate_triangle_area(base, height):
    error_messages = {
        'non_positive': "Base and height must be positive numbers.",
        'type_error': "Both base and height must be floating-point numbers."
    }
    
    if not isinstance(base, float) or not isinstance(height, float):
        raise TypeError(error_messages['type_error'])
    
    if base <= 0 or height <= 0:
        raise ValueError(error_messages['non_positive'])
    
    return 0.5 * base * height

if __name__ == '__main__':
    sample_values = {
        'base': 12.0,
        'height': 6.0
    }
    
    try:
        result = calculate_triangle_area(sample_values['base'], sample_values['height'])
        print(result)
    except Exception as e:
        print(e)