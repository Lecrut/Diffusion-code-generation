def convert_distance(value, unit):
    if unit == 'm':
        return value / 1000
    elif unit == 'km':
        return value * 1000
    else:
        raise ValueError("Unsupported unit. Use 'm' for meters or 'km' for kilometers.")

if __name__ == '__main__':
    distance_in_meters = 5000
    distance_in_kilometers = convert_distance(distance_in_meters, 'm')
    print(f"{distance_in_meters} meters is {distance_in_kilometers} kilometers")

    distance_in_kilometers = 3.5
    distance_in_meters = convert_distance(distance_in_kilometers, 'km')
    print(f"{distance_in_kilometers} kilometers is {distance_in_meters} meters")