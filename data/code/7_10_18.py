def convert_duration(value, unit):
    valid_units = ('seconds', 'minutes', 'hours', 'days')
    if unit not in valid_units:
        raise ValueError(f"Invalid unit: {unit}. Must be one of {valid_units}")
    if not isinstance(value, (int, float)):
        raise TypeError(f"Value must be a number, got {type(value).__name__}")
    if value < 0:
        raise ValueError(f"Duration cannot be negative: {value}")

    seconds = value
    if unit == 'minutes':
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
    sample_value = 5
    sample_unit = 'hours'
    result = convert_duration(sample_value, sample_unit)
    print(result)

    sample_value_2 = 2.5
    sample_unit_2 = 'days'
    result_2 = convert_duration(sample_value_2, sample_unit_2)
    print(result_2)

    try:
        convert_duration(10, 'weeks')
    except ValueError as e:
        print(str(e))

    try:
        convert_duration(-5, 'seconds')
    except ValueError as e:
        print(str(e))