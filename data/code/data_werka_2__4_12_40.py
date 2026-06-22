def convert_distance(value, unit):
    if unit == 'm_to_km':
        return value / 1000
    elif unit == 'km_to_m':
        return value * 1000
    else:
        raise ValueError("Unsupported conversion unit")

if __name__ == '__main__':
    distance_in_meters = 1500
    converted_to_km = convert_distance(distance_in_meters, 'm_to_km')
    print(f"{distance_in_meters} meters is {converted_to_km} kilometers")

    distance_in_kilometers = 2.5
    converted_to_meters = convert_distance(distance_in_kilometers, 'km_to_m')
    print(f"{distance_in_kilometers} kilometers is {converted_to_meters} meters")