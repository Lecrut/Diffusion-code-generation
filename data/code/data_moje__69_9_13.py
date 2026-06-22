def convert_miles_to_feet(mile_dict):
    return {key: value * 5280 for key, value in mile_dict.items()}

if __name__ == '__main__':
    sample_data = {'short_distance': 0.5, 'long_distance': 10.0, 'very_long': 2.25}
    result = convert_miles_to_feet(sample_data)
    print(result)