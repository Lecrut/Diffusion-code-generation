def convert_distance(distance, target_unit):
    if distance < 0:
        raise ValueError("Distance cannot be negative")
    
    conversion_factors = {
        'km_to_m': 1000,
        'm_to_km': 1 / 1000,
        'm_to_cm': 100,
        'cm_to_m': 1 / 100,
        'mi_to_km': 1.60934,
        'km_to_mi': 1 / 1.60934,
        'ft_to_m': 0.3048,
        'm_to_ft': 1 / 0.3048
    }
    
    if target_unit not in conversion_factors:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    
    factor = conversion_factors[target_unit]
    
    if factor == 0:
        raise ZeroDivisionError("Conversion factor is zero")
    
    return distance * factor

if __name__ == '__main__':
    sample_distance = 100
    sample_target = 'm_to_km'
    result = convert_distance(sample_distance, sample_target)
    print(result)
    
    sample_distance_2 = 5
    sample_target_2 = 'km_to_mi'
    result_2 = convert_distance(sample_distance_2, sample_target_2)
    print(result_2)