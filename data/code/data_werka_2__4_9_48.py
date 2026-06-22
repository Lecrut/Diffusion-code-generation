MILES_TO_KM = 1.60934

def adjust_distance(distance, unit):
    if unit == 'miles':
        adjusted_distance = distance * MILES_TO_KM
        new_unit = 'km'
    elif unit == 'km':
        adjusted_distance = distance / MILES_TO_KM
        new_unit = 'miles'
    else:
        raise ValueError("Unsupported unit type")
    return adjusted_distance, new_unit

if __name__ == '__main__':
    sample_distance_miles = 6
    adjusted_distance_km, new_unit_km = adjust_distance(sample_distance_miles, 'miles')
    print(f"{sample_distance_miles} miles is {adjusted_distance_km:.2f} {new_unit_km}")
    sample_distance_km = 15
    adjusted_distance_miles, new_unit_miles = adjust_distance(sample_distance_km, 'km')
    print(f"{sample_distance_km} km is {adjusted_distance_miles:.2f} {new_unit_miles}")