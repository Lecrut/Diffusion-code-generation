def meters_to_feet(meters):
    conversion_factor = 3.28084
    return meters * conversion_factor

if __name__ == '__main__':
    sample_value_meters = 10
    converted_value_feet = meters_to_feet(sample_value_meters)
    print(converted_value_feet)