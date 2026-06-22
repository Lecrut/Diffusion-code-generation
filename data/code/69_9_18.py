def convert_miles_to_feet(measurements):
    result = {}
    for key, value in measurements.items():
        result[key] = value * 5280
    return result

if __name__ == '__main__':
    sample_data = {
        "distance_a": 1.5,
        "distance_b": 2.75,
        "distance_c": 10,
        "distance_d": 0.05
    }
    converted_data = convert_miles_to_feet(sample_data)
    print(converted_data)