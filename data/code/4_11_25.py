def adjust_distance(distance, unit):
    if unit == 'miles':
        factor = 1.60934
        adjusted_distance = distance * factor
        return f"{adjusted_distance} km"
    elif unit == 'km':
        factor = 0.621371
        adjusted_distance = distance * factor
        return f"{adjusted_distance} miles"
    else:
        return "Invalid unit"

if __name__ == '__main__':
    sample_distance_miles = 5
    sample_unit_miles = 'miles'
    result_miles_to_km = adjust_distance(sample_distance_miles, sample_unit_miles)
    print(result_miles_to_km)

    sample_distance_km = 10
    sample_unit_km = 'km'
    result_km_to_miles = adjust_distance(sample_distance_km, sample_unit_km)
    print(result_km_to_miles)