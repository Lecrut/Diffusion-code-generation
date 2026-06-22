def adjust_distance(value, unit):
    conversion_factors = {
        'miles': 1.60934,
        'km': 0.621371,
        'kilometers': 0.621371,
        'mi': 1.60934
    }
    
    unit_lower = unit.lower()
    
    if unit_lower not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    
    if unit_lower == 'miles' or unit_lower == 'mi':
        result = value * conversion_factors['miles']
        new_unit = 'km'
    elif unit_lower == 'km' or unit_lower == 'kilometers':
        result = value * conversion_factors['km']
        new_unit = 'miles'
    
    return result, new_unit

if __name__ == '__main__':
    sample_distance = 10
    sample_unit = 'miles'
    adjusted_value, adjusted_unit = adjust_distance(sample_distance, sample_unit)
    print(f"{sample_distance} {sample_unit} is {adjusted_value:.2f} {adjusted_unit}")
    
    sample_distance_km = 50
    sample_unit_km = 'km'
    adjusted_value_km, adjusted_unit_km = adjust_distance(sample_distance_km, sample_unit_km)
    print(f"{sample_distance_km} {sample_unit_km} is {adjusted_value_km:.2f} {adjusted_unit_km}")