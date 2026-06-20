def convert_time(value, from_unit, to_unit):
    seconds_per_unit = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400,
        'weeks': 604800,
        'months': 2592000,
        'years': 31536000,
        'milliseconds': 0.001,
        'microseconds': 0.000001,
        'nanoseconds': 0.000000001
    }
    
    if from_unit not in seconds_per_unit:
        raise ValueError(f"Unknown from_unit: {from_unit}")
    if to_unit not in seconds_per_unit:
        raise ValueError(f"Unknown to_unit: {to_unit}")
    
    if value == 0:
        return 0
    
    value_in_seconds = value * seconds_per_unit[from_unit]
    converted_value = value_in_seconds / seconds_per_unit[to_unit]
    
    if converted_value.is_integer():
        return int(converted_value)
    return converted_value

if __name__ == '__main__':
    print(convert_time(1, 'hours', 'minutes'))
    print(convert_time(3600, 'seconds', 'hours'))
    print(convert_time(1.5, 'days', 'hours'))
    print(convert_time(1000, 'milliseconds', 'seconds'))
    print(convert_time(1, 'year', 'days'))