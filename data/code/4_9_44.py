def validate_unit(unit):
    supported_units = {'miles', 'km'}
    if unit not in supported_units:
        raise ValueError("Unsupported unit type")

def adjust_distance(distance, unit):
    validate_unit(unit)
    
    conversion_factors = {
        'miles': 1.60934,
        'km': 1 / 1.60934
    }
    
    adjusted_distance = distance * conversion_factors[unit]
    new_unit = 'km' if unit == 'miles' else 'miles'
    
    return adjusted_distance, new_unit

if __name__ == '__main__':
    sample_distance_miles = 5
    adjusted_distance_km, new_unit_km = adjust_distance(sample_distance_miles, 'miles')
    print(f"{sample_distance_miles} miles is {adjusted_distance_km:.2f} {new_unit_km}")
    
    sample_distance_km = 10
    adjusted_distance_miles, new_unit_miles = adjust_distance(sample_distance_km, 'km')
    print(f"{sample_distance_km} km is {adjusted_distance_miles:.2f} {new_unit_miles}")