def convert_duration(value, unit):
    valid_units = ['seconds', 'minutes', 'hours', 'days']
    if unit not in valid_units:
        raise ValueError(f"Invalid unit: {unit}. Must be one of {valid_units}")
    if not isinstance(value, (int, float)):
        raise TypeError(f"Value must be a number, got {type(value).__name__}")
    if value < 0:
        raise ValueError("Duration value cannot be negative")
    
    seconds = 0
    if unit == 'seconds':
        seconds = value
    elif unit == 'minutes':
        seconds = value * 60
    elif unit == 'hours':
        seconds = value * 3600
    elif unit == 'days':
        seconds = value * 86400
    
    result = {
        'seconds': seconds,
        'minutes': seconds / 60,
        'hours': seconds / 3600,
        'days': seconds / 86400
    }
    
    return result

def format_duration_result(result):
    lines = []
    for unit, value in result.items():
        formatted_value = value
        if value == int(value):
            formatted_value = int(value)
        lines.append(f"{unit}: {formatted_value}")
    return '\n'.join(lines)

if __name__ == '__main__':
    test_value = 5.5
    test_unit = 'hours'
    
    try:
        conversion = convert_duration(test_value, test_unit)
        print(format_duration_result(conversion))
        
        print("---")
        
        test_value2 = 7200
        test_unit2 = 'seconds'
        conversion2 = convert_duration(test_value2, test_unit2)
        print(format_duration_result(conversion2))
        
        print("---")
        
        test_value3 = 2
        test_unit3 = 'days'
        conversion3 = convert_duration(test_value3, test_unit3)
        print(format_duration_result(conversion3))
        
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")