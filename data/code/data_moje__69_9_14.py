def convert_miles_to_feet(measurements):
    conversion_factor = 5280
    return {key: value * conversion_factor for key, value in measurements.items()}

if __name__ == '__main__':
    sample_data = {'distance_a': 2.5, 'distance_b': 10, 'distance_c': 0.125}
    result = convert_miles_to_feet(sample_data)
    print(result)