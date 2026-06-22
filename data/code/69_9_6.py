def convert_miles_to_feet(measurements):
    return {key: value * 5280 for key, value in measurements.items()}

if __name__ == '__main__':
    sample_data = {'distance_a': 1.5, 'distance_b': 0.25, 'distance_c': 10}
    result = convert_miles_to_feet(sample_data)
    print(result)