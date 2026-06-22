def convert_miles_to_feet(measurements: dict) -> dict:
    return {key: value * 5280 for key, value in measurements.items()}

if __name__ == '__main__':
    sample_data = {'height': 3, 'width': 5, 'depth': 2.5}
    print(convert_miles_to_feet(sample_data))