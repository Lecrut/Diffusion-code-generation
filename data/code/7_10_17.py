def convert_time_duration(value, unit):
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

def validate_and_convert(value, unit):
    try:
        result = convert_time_duration(value, unit)
        return result
    except ValueError as e:
        return str(e)

if __name__ == '__main__':
    sample_value = 5
    sample_unit = 'hours'
    result = validate_and_convert(sample_value, sample_unit)
    print(result)