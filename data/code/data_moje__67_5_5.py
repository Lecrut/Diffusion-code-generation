def convert_liters_to_milliliters(measurements):
    conversion_factor = 1000
    return {key: value * conversion_factor if isinstance(value, (int, float)) else value for key, value in measurements.items()}

if __name__ == '__main__':
    sample_data = {'beaker_a': 2.5, 'flask_b': 10, 'cylinder_c': 0.75, 'note': 'static text'}
    result = convert_liters_to_milliliters(sample_data)
    print(result)