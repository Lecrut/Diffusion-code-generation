def convert_miles_to_feet(measurements):
    return {key: value * 5280 for key, value in measurements.items()}

if __name__ == '__main__':
    sample_data = {'short_distance': 1, 'medium_distance': 5, 'long_distance': 0.5, 'extra_long': 12.25}
    result = convert_miles_to_feet(sample_data)
    print(result)