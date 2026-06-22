def validate_unit(unit):
    if unit not in ['m', 'km']:
        raise ValueError("Unsupported unit. Use 'm' for meters or 'km' for kilometers.")

def convert_distance(value, unit):
    validate_unit(unit)
    if unit == 'm':
        return value / 1000
    elif unit == 'km':
        return value * 1000

if __name__ == '__main__':
    distance_in_meters = 3000
    try:
        distance_in_kilometers = convert_distance(distance_in_meters, 'm')
        print(f"{distance_in_meters} meters is {distance_in_kilometers} kilometers")
    except ValueError as e:
        print(e)

    distance_in_kilometers = 5.2
    try:
        distance_in_meters = convert_distance(distance_in_kilometers, 'km')
        print(f"{distance_in_kilometers} kilometers is {distance_in_meters} meters")
    except ValueError as e:
        print(e)