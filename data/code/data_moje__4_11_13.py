def adjust_distance(value, unit):
    if unit == 'miles':
        conversion_factor = 1.60934
        new_unit = 'km'
        result = value * conversion_factor
    elif unit == 'km':
        conversion_factor = 0.621371
        new_unit = 'miles'
        result = value * conversion_factor
    else:
        raise ValueError("Unit must be 'miles' or 'km'")
    print(f"Adjustment factor used: {conversion_factor}")
    return (result, new_unit)

if __name__ == '__main__':
    sample_distance = 10
    sample_unit = 'miles'
    adjusted_value, adjusted_unit = adjust_distance(sample_distance, sample_unit)
    print(f"Original: {sample_distance} {sample_unit}")
    print(f"Adjusted: {adjusted_value} {adjusted_unit}")

    sample_distance_2 = 50
    sample_unit_2 = 'km'
    adjusted_value_2, adjusted_unit_2 = adjust_distance(sample_distance_2, sample_unit_2)
    print(f"Original: {sample_distance_2} {sample_unit_2}")
    print(f"Adjusted: {adjusted_value_2} {adjusted_unit_2}")