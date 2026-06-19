def meters_to_feet(meters):
    conversion_factor = 3.28084
    return meters * conversion_factor

if __name__ == '__main__':
    sample_value_meters = 10
    sample_value_feet = meters_to_feet(sample_value_meters)
    print(f"{sample_value_meters} meters is equal to {sample_value_feet} feet")