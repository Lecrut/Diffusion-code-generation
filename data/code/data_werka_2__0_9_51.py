def convert_meters_to_feet(meters):
    if not isinstance(meters, (int, float)):
        raise ValueError("Input must be a numeric value.")
    conversion_factor = 3.28084
    return meters * conversion_factor

if __name__ == '__main__':
    sample_value = 10
    result = convert_meters_to_feet(sample_value)
    print(result)