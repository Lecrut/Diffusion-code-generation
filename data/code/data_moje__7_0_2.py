def convert_time(value, source_unit, target_unit):
    if source_unit == target_unit:
        return value
    
    units_to_seconds = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600
    }
    
    if source_unit not in units_to_seconds or target_unit not in units_to_seconds:
        raise ValueError("Unsupported unit. Choose from 'seconds', 'minutes', 'hours'.")
    
    seconds = value * units_to_seconds[source_unit]
    
    return seconds / units_to_seconds[target_unit]

if __name__ == '__main__':
    result = convert_time(2, 'hours', 'minutes')
    print(result)