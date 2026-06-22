def miles_to_feet(mile_dict):
    return {k: v * 5280 for k, v in mile_dict.items()}

if __name__ == '__main__':
    sample_data = {
        'distance_a': 1.5,
        'distance_b': 3.0,
        'distance_c': 0.25
    }
    result = miles_to_feet(sample_data)
    print(result)