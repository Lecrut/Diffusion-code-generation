def convert_time(value, source_unit, target_unit):
    units = ['s', 'sec', 'second', 'seconds', 'm', 'min', 'minute', 'minutes', 'h', 'hr', 'hour', 'hours']
    
    if source_unit not in units or target_unit not in units:
        raise ValueError(f"Invalid unit. Supported units: {units}")
    
    base_value = 0.0
    if source_unit in ['s', 'sec', 'second', 'seconds']:
        base_value = value
    elif source_unit in ['m', 'min', 'minute', 'minutes']:
        base_value = value * 60
    elif source_unit in ['h', 'hr', 'hour', 'hours']:
        base_value = value * 3600
    
    result_value = 0.0
    if target_unit in ['s', 'sec', 'second', 'seconds']:
        result_value = base_value
    elif target_unit in ['m', 'min', 'minute', 'minutes']:
        result_value = base_value / 60
    elif target_unit in ['h', 'hr', 'hour', 'hours']:
        result_value = base_value / 3600
    
    return result_value

if __name__ == '__main__':
    print(convert_time(60, 'm', 's'))
    print(convert_time(3600, 's', 'h'))
    print(convert_time(2, 'h', 'm'))
    print(convert_time(90, 'min', 'h'))