def convert_time(value, from_unit, to_unit):
    conversions = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400,
        'weeks': 604800,
        'months': 2592000,
        'years': 31536000
    }
    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError("Invalid time unit")
    
    value_in_seconds = value * conversions[from_unit]
    result = value_in_seconds / conversions[to_unit]
    return result

if __name__ == '__main__':
    result = convert_time(1, 'hours', 'minutes')
    print(result)