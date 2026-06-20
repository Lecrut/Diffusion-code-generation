def convert_time_duration(value, unit):
    valid_units = {'seconds', 'minutes', 'hours', 'days'}
    if unit not in valid_units:
        raise ValueError(f"Invalid unit: {unit}. Must be one of {valid_units}")
    if value < 0:
        raise ValueError("Value must be non-negative")
    
    to_seconds = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400
    }
    
    total_seconds = value * to_seconds[unit]
    
    result = {
        'seconds': total_seconds,
        'minutes': total_seconds / 60,
        'hours': total_seconds / 3600,
        'days': total_seconds / 86400
    }
    
    return result

if __name__ == '__main__':
    sample_value = 5
    sample_unit = 'hours'
    conversions = convert_time_duration(sample_value, sample_unit)
    print(conversions)
    
    sample_value2 = 2
    sample_unit2 = 'days'
    conversions2 = convert_time_duration(sample_value2, sample_unit2)
    print(conversions2)
    
    try:
        convert_time_duration(1, 'weeks')
    except ValueError as e:
        print(str(e))
        
    try:
        convert_time_duration(-1, 'hours')
    except ValueError as e:
        print(str(e))