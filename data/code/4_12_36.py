def convert_distance(value, unit):
    if unit == 'm':
        return value / 1000
    elif unit == 'km':
        return value * 1000
    else:
        raise ValueError("Unsupported unit. Use 'm' for meters or 'km' for kilometers.")

if __name__ == '__main__':
    sample_meters = 1500
    sample_kilometers = 2.5

    converted_to_km = convert_distance(sample_meters, 'm')
    converted_to_m = convert_distance(sample_kilometers, 'km')

    print(f"{sample_meters} meters is {converted_to_km} kilometers")
    print(f"{sample_kilometers} kilometers is {converted_to_m} meters")