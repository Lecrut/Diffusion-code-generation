def convert_distance(value, from_unit, to_unit, miles_to_km_factor=1.60934):
    if from_unit == to_unit:
        return value
    if from_unit == 'miles' and to_unit == 'kilometers':
        return value * miles_to_km_factor
    if from_unit == 'kilometers' and to_unit == 'miles':
        return value / miles_to_km_factor
    raise ValueError(f"Unsupported units: {from_unit} to {to_unit}")

if __name__ == '__main__':
    distance_miles = 10.0
    converted_km = convert_distance(distance_miles, 'miles', 'kilometers')
    print(converted_km)
    distance_km = 16.0934
    converted_miles = convert_distance(distance_km, 'kilometers', 'miles')
    print(converted_miles)