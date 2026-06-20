def adjust_distance(distance, unit_type):
    conversion_factors = {
        'miles': 1.60934,
        'km': 0.621371
    }
    
    if unit_type not in conversion_factors:
        raise ValueError("Unit must be 'miles' or 'km'")
    
    if unit_type == 'miles':
        factor = conversion_factors[unit_type]
        converted_value = distance * factor
        new_unit = 'km'
    else:
        factor = conversion_factors[unit_type]
        converted_value = distance * factor
        new_unit = 'miles'
    
    result = {
        'original_distance': distance,
        'original_unit': unit_type,
        'conversion_factor': factor,
        'converted_distance': converted_value,
        'new_unit': new_unit
    }
    
    return result

if __name__ == '__main__':
    distance_to_adjust = 10.0
    unit_to_adjust = 'miles'
    
    result = adjust_distance(distance_to_adjust, unit_to_adjust)
    
    print(f"Adjusted distance: {result['converted_distance']} {result['new_unit']}")
    print(f"Conversion factor used: {result['conversion_factor']}")