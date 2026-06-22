def adjust_distance(distance, unit):
    miles_to_km_factor = 1.60934
    km_to_miles_factor = 1 / miles_to_km_factor

    if unit == 'miles':
        adjusted_value = distance * miles_to_km_factor
        target_unit = 'km'
        factor_used = miles_to_km_factor
    elif unit == 'km':
        adjusted_value = distance * km_to_miles_factor
        target_unit = 'miles'
        factor_used = km_to_miles_factor
    else:
        adjusted_value = distance
        target_unit = unit
        factor_used = 1.0

    return adjusted_value, factor_used, target_unit

if __name__ == '__main__':
    original_distance = 10.0
    original_unit = 'miles'
    result, factor, target = adjust_distance(original_distance, original_unit)
    print((result, factor, target))