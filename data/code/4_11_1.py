def adjust_distance(distance, unit_type):
    if unit_type == 'miles':
        return distance * 1.609344
    elif unit_type == 'km':
        return distance / 1.609344
    else:
        raise ValueError("Invalid unit type. Use 'miles' or 'km'.")

if __name__ == '__main__':
    sample_distance = 10
    sample_unit = 'miles'
    result = adjust_distance(sample_distance, sample_unit)
    print(result)
    sample_distance_km = 16.09344
    sample_unit_km = 'km'
    result_km = adjust_distance(sample_distance_km, sample_unit_km)
    print(result_km)