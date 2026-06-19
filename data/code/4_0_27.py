def convert_distance(value, from_unit, to_unit):
    conversion_factors = {'m': {'km': 0.001, 'mi': 0.000621371}, 'km': {'m': 1000, 'mi': 0.621371}, 'mi': {'m': 1609.34, 'km': 1.60934}}
    if from_unit not in conversion_factors or to_unit not in conversion_factors[from_unit]:
        raise ValueError('Invalid unit conversion')
    return value * conversion_factors[from_unit][to_unit]
if __name__ == '__main__':
    distance_meters = 1000
    distance_kilometers = 5
    distance_miles = 3
    converted_to_km = convert_distance(distance_meters, 'm', 'km')
    print(f'{distance_meters} meters is {converted_to_km} kilometers')
    converted_to_mi = convert_distance(distance_kilometers, 'km', 'mi')
    print(f'{distance_kilometers} kilometers is {converted_to_mi} miles')
    converted_to_m = convert_distance(distance_miles, 'mi', 'm')
    print(f'{distance_miles} miles is {converted_to_m} meters')