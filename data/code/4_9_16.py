def convert_distance(value, from_unit, to_unit):
    miles_to_km = 1.60934
    km_to_miles = 1 / miles_to_km

    if from_unit == 'miles' and to_unit == 'kilometers':
        return value * miles_to_km
    elif from_unit == 'kilometers' and to_unit == 'miles':
        return value * km_to_miles
    elif from_unit == to_unit:
        return value
    else:
        raise ValueError(f"Unsupported units: {from_unit} to {to_unit}")

if __name__ == '__main__':
    miles_value = 10
    km_value = 16.0934

    result1 = convert_distance(miles_value, 'miles', 'kilometers')
    print(result1)

    result2 = convert_distance(km_value, 'kilometers', 'miles')
    print(result2)

    result3 = convert_distance(5, 'miles', 'miles')
    print(result3)