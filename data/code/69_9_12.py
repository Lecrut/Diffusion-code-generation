def convert_miles_to_feet(measurements: dict) -> dict:
    result = {}
    for key, value in measurements.items():
        result[key] = value * 5280
    return result

if __name__ == '__main__':
    sample_data = {"road_length": 3.5, "track_length": 10, "short_path": 0.1}
    converted_data = convert_miles_to_feet(sample_data)
    print(converted_data)