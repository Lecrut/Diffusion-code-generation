def convert_time_to_minutes(time_str):
    if not isinstance(time_str, str) or len(time_str) != 5 or time_str[2] != ':':
        raise ValueError('Invalid time format')
    
    parts = time_str.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    
    if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
        raise ValueError('Invalid time range')
    
    return hours * 60 + minutes

if __name__ == '__main__':
    try:
        result = convert_time_to_minutes('14:30')
        print(result)
    except ValueError as e:
        print(e)

    try:
        result = convert_time_to_minutes('23:59')
        print(result)
    except ValueError as e:
        print(e)

    try:
        result = convert_time_to_minutes('00:00')
        print(result)
    except ValueError as e:
        print(e)

    try:
        result = convert_time_to_minutes('12:60')
        print(result)
    except ValueError as e:
        print(e)

    try:
        result = convert_time_to_minutes('24:00')
        print(result)
    except ValueError as e:
        print(e)

    try:
        result = convert_time_to_minutes('14-30')
        print(result)
    except ValueError as e:
        print(e)