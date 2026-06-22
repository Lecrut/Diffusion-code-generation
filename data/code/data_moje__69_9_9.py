def convert_miles_to_feet(miles_dict):
    return {key: value * 5280 for key, value in miles_dict.items()}

if __name__ == '__main__':
    sample_miles = {'distance_a': 1, 'distance_b': 2.5, 'distance_c': 0.5}
    print(convert_miles_to_feet(sample_miles))