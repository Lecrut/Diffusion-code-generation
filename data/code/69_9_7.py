def convert_miles_to_feet(measurements):
    return {key: value * 5280 for key, value in measurements.items()}

if __name__ == '__main__':
    sample_data = {'distance_to_park': 2.5, 'marathon_length': 26.2, 'short_walk': 0.1}
    converted_data = convert_miles_to_feet(sample_data)
    print(converted_data)