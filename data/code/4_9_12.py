def convert_distance(value, from_unit, to_unit, conversion_factor):
    if from_unit == to_unit:
        return value
    if from_unit == 'miles' and to_unit == 'kilometers':
        return value * conversion_factor
    if from_unit == 'kilometers' and to_unit == 'miles':
        return value / conversion_factor
    raise ValueError('Unsupported unit combination')

if __name__ == '__main__':
    sample_distance_miles = 100
    sample_distance_km = 160.934
    conversion_rate = 1.60934
    result_km = convert_distance(sample_distance_miles, 'miles', 'kilometers', conversion_rate)
    result_miles = convert_distance(sample_distance_km, 'kilometers', 'miles', conversion_rate)
    print(f'{sample_distance_miles} miles is {result_km} kilometers')
    print(f'{sample_distance_km} kilometers is {result_miles} miles')