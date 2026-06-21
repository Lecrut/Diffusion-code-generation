def convert_meters_to_feet(meters):
    conversion_factor = 3.28084
    return meters * conversion_factor

if __name__ == '__main__':
    sample_length_in_meters = 15
    converted_length_in_feet = convert_meters_to_feet(sample_length_in_meters)
    print(converted_length_in_feet)