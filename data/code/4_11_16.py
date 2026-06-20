def adjust_distance(value, unit):
    factors = {
        'miles': 1.60934,
        'km': 0.621371,
        'kilometers': 0.621371,
        'kilometres': 0.621371,
        'mile': 1.60934,
        'km': 0.621371
    }
    unit_lower = unit.lower()
    if unit_lower == 'miles' or unit_lower == 'mile':
        return value * 1.60934
    elif unit_lower == 'km' or unit_lower == 'kilometers' or unit_lower == 'kilometres':
        return value * 0.621371
    else:
        raise ValueError("Unsupported unit type")

if __name__ == '__main__':
    test_distance_miles = 10
    test_distance_km = 5
    result_miles_to_km = adjust_distance(test_distance_miles, 'miles')
    result_km_to_miles = adjust_distance(test_distance_km, 'km')
    print(result_miles_to_km)
    print(result_km_to_miles)