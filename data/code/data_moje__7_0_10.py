def convert_time(value, source_unit, target_unit):
    units = ['seconds', 'minutes', 'hours']
    source_unit = source_unit.lower()
    target_unit = target_unit.lower()
    
    if source_unit not in units or target_unit not in units:
        raise ValueError(f"Invalid unit. Supported units are: {units}")
    
    seconds_per_unit = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600
    }
    
    value_in_seconds = value * seconds_per_unit[source_unit]
    result = value_in_seconds / seconds_per_unit[target_unit]
    return result

if __name__ == '__main__':
    print(convert_time(60, 'minutes', 'seconds'))
    print(convert_time(180, 'seconds', 'minutes'))
    print(convert_time(2, 'hours', 'minutes'))
    print(convert_time(90, 'minutes', 'hours'))