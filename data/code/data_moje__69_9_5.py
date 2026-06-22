def miles_to_feet(miles_dict):
    return {key: value * 5280 for key, value in miles_dict.items()}

if __name__ == '__main__':
    sample_data = {
        'distance_a': 1,
        'distance_b': 2.5,
        'distance_c': 0.5
    }
    result = miles_to_feet(sample_data)
    print(result)