def convert_miles_to_feet(measurements):
    result = {}
    for key, value in measurements.items():
        result[key] = value * 5280
    return result

if __name__ == '__main__':
    sample_data = {
        "distance_a": 2.5,
        "distance_b": 0.75,
        "distance_c": 10
    }
    converted_data = convert_miles_to_feet(sample_data)
    print(converted_data)