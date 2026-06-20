def convert_distance(value, unit):
    MILE_TO_KM = 1.60934
    if unit == 'miles':
        return value * MILE_TO_KM
    elif unit == 'kilometers':
        return value / MILE_TO_KM
    else:
        raise ValueError("Unit must be 'miles' or 'kilometers'")

if __name__ == '__main__':
    sample_miles = 60
    sample_kilometers = 100
    result_miles_to_km = convert_distance(sample_miles, 'miles')
    result_km_to_miles = convert_distance(sample_kilometers, 'kilometers')
    print(result_miles_to_km)
    print(result_km_to_miles)