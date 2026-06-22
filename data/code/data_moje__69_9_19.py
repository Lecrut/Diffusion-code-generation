def miles_to_feet(miles_dict):
    return {k: v * 5280 for k, v in miles_dict.items()}

if __name__ == '__main__':
    sample = {
        'distance_a': 1,
        'distance_b': 2.5,
        'distance_c': 0
    }
    print(miles_to_feet(sample))