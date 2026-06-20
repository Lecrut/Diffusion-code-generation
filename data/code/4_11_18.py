def adjust_distance(distance, unit):
    conversion_factors = {
        'miles': {'factor': 1.60934, 'to': 'km'},
        'km': {'factor': 0.621371, 'to': 'miles'}
    }
    
    if unit not in conversion_factors:
        raise ValueError("Unit must be 'miles' or 'km'")
    
    info = conversion_factors[unit]
    adjusted_value = distance * info['factor']
    target_unit = info['to']
    
    return adjusted_value, info['factor'], target_unit

if __name__ == '__main__':
    val, factor, unit = adjust_distance(10, 'miles')
    print(val, factor, unit)
    val2, factor2, unit2 = adjust_distance(15, 'km')
    print(val2, factor2, unit2)