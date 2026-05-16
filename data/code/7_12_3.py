def convert_time(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'seconds':
        value_in_seconds = value
    elif from_unit == 'minutes':
        value_in_seconds = value * 60
    elif from_unit == 'hours':
        value_in_seconds = value * 3600
    elif from_unit == 'days':
        value_in_seconds = value * 86400
    else:
        raise ValueError("Unsupported 'from_unit'")
    if to_unit == 'seconds':
        return value_in_seconds
    elif to_unit == 'minutes':
        return value_in_seconds / 60
    elif to_unit == 'hours':
        return value_in_seconds / 3600
    elif to_unit == 'days':
        return value_in_seconds / 86400
    else:
        raise ValueError("Unsupported 'to_unit'")
if __name__ == '__main__':
    print(convert_time(3600, 'seconds', 'minutes'))
    print(convert_time(120, 'minutes', 'hours'))
    print(convert_time(86400, 'seconds', 'days'))
    print(convert_time(3600, 'hours', 'days'))
    print(convert_time(7200, 'minutes', 'seconds'))
    print(convert_time(10, 'days', 'hours'))
    try:
        convert_time(10, 'years', 'days')
    except ValueError as e:
        print(f"Error: {e}")