def convert_distance(value, from_unit, to_unit, factor=1.60934):
    if from_unit == 'miles' and to_unit == 'kilometers':
        return value * factor
    elif from_unit == 'kilometers' and to_unit == 'miles':
        return value / factor
    else:
        return value

if __name__ == '__main__':
    miles_to_km = convert_distance(50, 'miles', 'kilometers', 1.60934)
    km_to_miles = convert_distance(80.467, 'kilometers', 'miles', 1.60934)
    print(miles_to_km)
    print(km_to_miles)