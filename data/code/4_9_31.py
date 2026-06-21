def adjust_distance(distance, unit):
    conversion_factors = {
        'miles_to_km': 1.60934,
        'km_to_miles': 1 / 1.60934
    }
    
    if unit == 'miles':
        adjusted_distance = distance * conversion_factors['miles_to_km']
        new_unit = 'km'
    elif unit == 'km':
        adjusted_distance = distance * conversion_factors['km_to_miles']
        new_unit = 'miles'
    else:
        raise ValueError("Unsupported unit type")
    
    return adjusted_distance, new_unit

if __name__ == '__main__':
    sample_distance_miles = 7
    adjusted_distance_km, new_unit_km = adjust_distance(sample_distance_miles, 'miles')
    print(f"{sample_distance_miles} miles is {adjusted_distance_km:.2f} {new_unit_km}")
    
    sample_distance_km = 15
    adjusted_distance_miles, new_unit_miles = adjust_distance(sample_distance_km, 'km')
    print(f"{sample_distance_km} km is {adjusted_distance_miles:.2f} {new_unit_miles}")