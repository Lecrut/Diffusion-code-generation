def convert_time(value, source_unit, target_unit):
    if source_unit not in ('seconds', 'minutes', 'hours') or target_unit not in ('seconds', 'minutes', 'hours'):
        raise ValueError("Unsupported unit. Choose from 'seconds', 'minutes', 'hours'.")
    
    if source_unit == target_unit:
        return value
    
    if source_unit == 'minutes':
        value *= 60
        source_unit = 'seconds'
    elif source_unit == 'hours':
        value *= 3600
        source_unit = 'seconds'
    
    if target_unit == 'seconds':
        return value
    elif target_unit == 'minutes':
        return value / 60
    elif target_unit == 'hours':
        return value / 3600

if __name__ == '__main__':
    result = convert_time(3.5, 'hours', 'minutes')
    print(result)