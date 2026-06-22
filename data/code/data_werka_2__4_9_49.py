def adjust_distance(distance, unit):
    conversion_factors = {
        'miles_to_km': 1.60934,
        'km_to_miles': 1 / 1.60934
    }
    
    if unit == 'miles':
        key = 'miles_to_km'
    elif unit == 'km':
        key = 'km_to_miles'
    else:
        raise ValueError("Unsupported unit type")
    
    adjusted_distance = distance * conversion_factors[key]
    new_unit = 'km' if unit == 'miles' else 'miles'
    
    return adjusted_distance, new_unit

if __name__ == '__main__':
    sample_distance_miles = 10
    adjusted_distance_km, new_unit_km = adjust_distance(sample_distance_miles, 'miles')
    print(f"{sample_distance_miles} miles is {adjusted_distance_km:.2f} {new_unit_km}")
    
    sample_distance_km = 16.0934
    adjusted_distance_miles, new_unit_miles = adjust_distance(sample_distance_km, 'km')
    print(f"{sample_distance_km} km is {adjusted_distance_miles:.2f} {new_unit_miles}")