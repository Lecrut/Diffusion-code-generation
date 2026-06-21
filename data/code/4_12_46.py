def convert_distance(value, unit):
    if unit == 'meters_to_kilometers':
        return value / 1000
    elif unit == 'kilometers_to_meters':
        return value * 1000
    else:
        raise ValueError("Unsupported conversion unit")

if __name__ == '__main__':
    sample_value_meters = 2500
    sample_value_kilometers = 3.5

    converted_to_km = convert_distance(sample_value_meters, 'meters_to_kilometers')
    converted_to_m = convert_distance(sample_value_kilometers, 'kilometers_to_meters')

    print(f"{sample_value_meters} meters is {converted_to_km} kilometers")
    print(f"{sample_value_kilometers} kilometers is {converted_to_m} meters")