def convert_distance(distance, from_unit, to_unit, conversion_factor):
    if from_unit == 'miles' and to_unit == 'kilometers':
        return distance * conversion_factor
    elif from_unit == 'kilometers' and to_unit == 'miles':
        return distance / conversion_factor
    else:
        raise ValueError('Unsupported unit conversion')
if __name__ == '__main__':
    distance_miles = 10.0
    distance_kilometers = 16.0934
    miles_to_km_conversion_factor = 1.60934
    converted_distance_km = convert_distance(distance_miles, 'miles', 'kilometers', miles_to_km_conversion_factor)
    print(f'{distance_miles} miles is {converted_distance_km:.2f} kilometers')
    converted_distance_miles = convert_distance(distance_kilometers, 'kilometers', 'miles', miles_to_km_conversion_factor)
    print(f'{distance_kilometers} kilometers is {converted_distance_miles:.2f} miles')