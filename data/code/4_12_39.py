def convert_distance(value, unit):
    conversion_factors = {'m': 1 / 1000, 'km': 1000}
    if unit not in conversion_factors:
        raise ValueError("Unsupported unit. Use 'm' for meters or 'km' for kilometers.")
    return value * conversion_factors[unit]
if __name__ == '__main__':
    distance_meters = 3000
    distance_kilometers = convert_distance(distance_meters, 'm')
    print(f'{distance_meters} meters is {distance_kilometers} kilometers')
    distance_kilometers = 5.5
    distance_meters = convert_distance(distance_kilometers, 'km')
    print(f'{distance_kilometers} kilometers is {distance_meters} meters')