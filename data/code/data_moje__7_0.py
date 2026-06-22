def convert_time(value, source_unit, target_unit):
    source_unit = source_unit.lower()
    target_unit = target_unit.lower()
    
    if source_unit not in ('seconds', 'minutes', 'hours') or target_unit not in ('seconds', 'minutes', 'hours'):
        raise ValueError("Invalid unit. Use 'seconds', 'minutes', or 'hours'.")
    
    if source_unit == target_unit:
        return value
    
    value_in_seconds = 0
    if source_unit == 'seconds':
        value_in_seconds = value
    elif source_unit == 'minutes':
        value_in_seconds = value * 60
    elif source_unit == 'hours':
        value_in_seconds = value * 3600
    
    if target_unit == 'seconds':
        return value_in_seconds
    elif target_unit == 'minutes':
        return value_in_seconds / 60
    elif target_unit == 'hours':
        return value_in_seconds / 3600

if __name__ == '__main__':
    result1 = convert_time(1, 'hours', 'minutes')
    result2 = convert_time(90, 'minutes', 'hours')
    result3 = convert_time(3600, 'seconds', 'hours')
    print(result1)
    print(result2)
    print(result3)