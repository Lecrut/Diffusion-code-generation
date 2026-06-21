def meters_to_feet(meters):
    conversion_factor = 3.28084
    return meters * conversion_factor

if __name__ == '__main__':
    sample_value_meters = 15
    result_feet = meters_to_feet(sample_value_meters)
    print(result_feet)