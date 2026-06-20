def convert_duration(value, unit):
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a number")
    if value < 0:
        raise ValueError("Value must be non-negative")
    
    valid_units = ('seconds', 'minutes', 'hours', 'days')
    if unit not in valid_units:
        raise ValueError(f"Unit must be one of {valid_units}")
    
    seconds = 0
    if unit == 'seconds':
        seconds = value
    elif unit == 'minutes':
        seconds = value * 60
    elif unit == 'hours':
        seconds = value * 3600
    elif unit == 'days':
        seconds = value * 86400
    
    return {
        'seconds': seconds,
        'minutes': seconds / 60,
        'hours': seconds / 3600,
        'days': seconds / 86400
    }

if __name__ == '__main__':
    result1 = convert_duration(1, 'hours')
    print(result1)
    
    result2 = convert_duration(90, 'minutes')
    print(result2)
    
    result3 = convert_duration(2.5, 'days')
    print(result3)
    
    try:
        convert_duration(-5, 'seconds')
    except ValueError as e:
        print(str(e))
    
    try:
        convert_duration(10, 'weeks')
    except ValueError as e:
        print(str(e))