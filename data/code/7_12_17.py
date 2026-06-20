def convert_time(value, from_unit, to_unit):
    seconds_per_unit = {
        'seconds': 1,
        'second': 1,
        's': 1,
        'milliseconds': 1000,
        'millisecond': 1000,
        'ms': 1000,
        'minutes': 60,
        'minute': 60,
        'min': 60,
        'mins': 60,
        'hours': 3600,
        'hour': 3600,
        'h': 3600,
        'hrs': 3600,
        'days': 86400,
        'day': 86400,
        'd': 86400
    }
    
    value_in_seconds = value * seconds_per_unit.get(from_unit, 1)
    result = value_in_seconds / seconds_per_unit.get(to_unit, 1)
    return result

if __name__ == '__main__':
    result = convert_time(1, 'hours', 'seconds')
    print(result)
    
    result2 = convert_time(3600, 'seconds', 'hours')
    print(result2)
    
    result3 = convert_time(1.5, 'days', 'hours')
    print(result3)