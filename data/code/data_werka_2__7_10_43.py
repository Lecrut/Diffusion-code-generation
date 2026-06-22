def convert_time(value, from_unit, to_unit):
    time_units = {
        'second': 1,
        'minute': 60,
        'hour': 3600,
        'day': 86400,
        'week': 604800,
        'month': 2592000,
        'year': 31536000
    }
    
    if from_unit not in time_units or to_unit not in time_units:
        raise ValueError("Unsupported unit. Please choose from 'second', 'minute', 'hour', 'day', 'week', 'month', 'year'.")
    
    value_in_seconds = value * time_units[from_unit]
    converted_value = value_in_seconds / time_units[to_unit]
    return converted_value

if __name__ == '__main__':
    print(convert_time(1, 'minute', 'second'))
    print(convert_time(24, 'hour', 'day'))
    print(convert_time(52, 'week', 'year'))
    print(convert_time(3600, 'second', 'hour'))