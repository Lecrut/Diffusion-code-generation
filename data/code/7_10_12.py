def convert_time(duration, unit):
    valid_units = {'seconds', 'minutes', 'hours', 'days'}
    if unit not in valid_units:
        raise ValueError(f"Invalid unit '{unit}'. Must be one of {valid_units}.")
    if not isinstance(duration, (int, float)) or duration < 0:
        raise ValueError("Duration must be a non-negative number.")
    
    conversion_factors = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400
    }
    
    total_seconds = duration * conversion_factors[unit]
    
    result = {
        'seconds': total_seconds,
        'minutes': total_seconds / 60,
        'hours': total_seconds / 3600,
        'days': total_seconds / 86400
    }
    
    return result

if __name__ == '__main__':
    sample_duration = 2.5
    sample_unit = 'hours'
    converted_values = convert_time(sample_duration, sample_unit)
    print(converted_values)