def convert_duration(value, unit):
    units_map = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400
    }
    
    if unit not in units_map:
        raise ValueError(f"Invalid unit: {unit}. Must be one of {list(units_map.keys())}")
    
    if value < 0:
        raise ValueError("Value must be non-negative")
    
    total_seconds = value * units_map[unit]
    
    converted = {
        'seconds': total_seconds,
        'minutes': total_seconds / 60,
        'hours': total_seconds / 3600,
        'days': total_seconds / 86400
    }
    
    return converted

if __name__ == '__main__':
    sample_value = 5
    sample_unit = 'hours'
    
    result = convert_duration(sample_value, sample_unit)
    print(result)