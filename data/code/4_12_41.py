def convert_distance(value, unit):
    if unit == 'm':
        return value / 1000
    elif unit == 'km':
        return value * 1000
    else:
        raise ValueError("Unsupported unit. Use 'm' for meters or 'km' for kilometers.")

if __name__ == '__main__':
    distance_meters = 5000
    distance_kilometers = 3

    converted_to_km = convert_distance(distance_meters, 'm')
    converted_to_m = convert_distance(distance_kilometers, 'km')

    print(f"{distance_meters} meters is {converted_to_km} kilometers.")
    print(f"{distance_kilometers} kilometers is {converted_to_m} meters.")