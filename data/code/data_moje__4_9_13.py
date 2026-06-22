def convert_distance(value, from_unit, to_unit):
    miles_to_km = 1.60934
    km_to_miles = 0.621371

    if from_unit == 'miles' and to_unit == 'km':
        return value * miles_to_km
    elif from_unit == 'km' and to_unit == 'miles':
        return value * km_to_miles
    elif from_unit == to_unit:
        return value
    else:
        raise ValueError(f"Unsupported unit conversion from {from_unit} to {to_unit}")

if __name__ == '__main__':
    sample_miles = 10.0
    sample_km = 16.0934

    result_miles_to_km = convert_distance(sample_miles, 'miles', 'km')
    print(result_miles_to_km)

    result_km_to_miles = convert_distance(sample_km, 'km', 'miles')
    print(result_km_to_miles)

    result_same_unit = convert_distance(sample_miles, 'miles', 'miles')
    print(result_same_unit)