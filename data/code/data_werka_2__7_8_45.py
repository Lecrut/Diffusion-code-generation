def convert_time(duration, unit):
    if not isinstance(duration, (int, float)):
        raise ValueError("Duration must be a number.")
    if duration < 0:
        raise ValueError("Duration cannot be negative.")
    
    UNIT_CONVERSIONS = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400
    }
    
    if unit not in UNIT_CONVERSIONS:
        raise ValueError(f"Unsupported unit: {unit}")
    
    total_seconds = duration * UNIT_CONVERSIONS[unit]
    
    converted_values = {
        'seconds': total_seconds,
        'minutes': total_seconds / UNIT_CONVERSIONS['minutes'],
        'hours': total_seconds / UNIT_CONVERSIONS['hours'],
        'days': total_seconds / UNIT_CONVERSIONS['days']
    }
    
    return converted_values

if __name__ == '__main__':
    sample_duration = 48
    sample_unit = 'hours'
    result = convert_time(sample_duration, sample_unit)
    print(result)