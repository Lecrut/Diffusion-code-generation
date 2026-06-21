def adjust_distance(distance, unit):
    conversion_factors = {
        'miles': 1.60934,
        'km': 1 / 1.60934
    }
    
    if unit not in conversion_factors:
        raise ValueError("Unsupported unit type")
    
    adjusted_distance = distance * conversion_factors[unit]
    new_unit = 'km' if unit == 'miles' else 'miles'
    
    return adjusted_distance, new_unit

if __name__ == '__main__':
    sample_distance_miles = 3
    adjusted_distance_km, new_unit_km = adjust_distance(sample_distance_miles, 'miles')
    print(f"{sample_distance_miles} miles is {adjusted_distance_km:.2f} {new_unit_km}")
    
    sample_distance_km = 8
    adjusted_distance_miles, new_unit_miles = adjust_distance(sample_distance_km, 'km')
    print(f"{sample_distance_km} km is {adjusted_distance_miles:.2f} {new_unit_miles}")