def miles_to_feet(mile_measurements):
    return {k: v * 5280 for k, v in mile_measurements.items()}

if __name__ == '__main__':
    sample_data = {'distance_a': 1.0, 'distance_b': 2.5, 'distance_c': 0.5}
    result = miles_to_feet(sample_data)
    print(result)