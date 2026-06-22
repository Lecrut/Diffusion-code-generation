def convert_distance(distance, target_unit, base_unit='meters', conversion_factors=None):
    if conversion_factors is None:
        conversion_factors = {
            'meters': 1.0,
            'kilometers': 1000.0,
            'centimeters': 0.01,
            'millimeters': 0.001,
            'inches': 0.0254,
            'feet': 0.3048,
            'yards': 0.9144,
            'miles': 1609.344,
            'nautical_miles': 1852.0
        }

    if target_unit not in conversion_factors:
        raise ValueError(f"Unsupported target unit: {target_unit}")

    if target_unit == base_unit:
        return float(distance)

    distance_in_base = float(distance) / conversion_factors.get(target_unit, 1.0)
    
    if target_unit != base_unit:
        for unit, factor in conversion_factors.items():
            if unit == target_unit:
                distance_in_base = float(distance) * factor
                break
    
    return distance_in_base / conversion_factors[target_unit] * conversion_factors[base_unit]

def safe_convert_distance(distance, target_unit):
    try:
        if target_unit is None or target_unit == '':
            raise ValueError("Target unit cannot be empty or None")
        
        factors = {
            'm': 1.0,
            'km': 0.001,
            'cm': 100.0,
            'mm': 1000.0,
            'in': 39.37007874,
            'ft': 3.280839895,
            'yd': 1.093613298,
            'mi': 0.000621371,
            'nm': 0.000539957
        }
        
        if target_unit not in factors:
            raise ValueError(f"Invalid target unit: {target_unit}")
            
        target_factor = factors[target_unit]
        if target_factor == 0:
            return 0.0
            
        result = float(distance) / target_factor
        return result
        
    except ZeroDivisionError:
        return 0.0
    except (ValueError, TypeError, KeyError):
        return 0.0

if __name__ == '__main__':
    sample_distance = 100.0
    sample_target = 'inches'
    result = safe_convert_distance(sample_distance, sample_target)
    print(result)
    
    sample_distance_2 = 5280.0
    sample_target_2 = 'miles'
    result_2 = safe_convert_distance(sample_distance_2, sample_target_2)
    print(result_2)
    
    sample_distance_3 = 0.0
    sample_target_3 = 'meters'
    result_3 = safe_convert_distance(sample_distance_3, sample_target_3)
    print(result_3)
    
    sample_distance_4 = 100.0
    sample_target_4 = 'invalid_unit'
    result_4 = safe_convert_distance(sample_distance_4, sample_target_4)
    print(result_4)
    
    sample_distance_5 = 100.0
    sample_target_5 = ''
    result_5 = safe_convert_distance(sample_distance_5, sample_target_5)
    print(result_5)