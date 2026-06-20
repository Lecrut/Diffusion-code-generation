def convert_time(value, from_unit, to_unit):
    units = {
        'second': 1,
        'sec': 1,
        's': 1,
        'minute': 60,
        'min': 60,
        'm': 60,
        'hour': 3600,
        'hr': 3600,
        'h': 3600,
        'day': 86400,
        'd': 86400,
        'week': 604800,
        'wk': 604800,
        'w': 604800,
        'month': 2629746,
        'mo': 2629746,
        'year': 31556952,
        'yr': 31556952,
        'y': 31556952,
    }

    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()

    if from_unit_lower not in units:
        raise ValueError(f"Invalid from_unit: {from_unit}")
    if to_unit_lower not in units:
        raise ValueError(f"Invalid to_unit: {to_unit}")

    seconds = value * units[from_unit_lower]
    result = seconds / units[to_unit_lower]
    return result

if __name__ == '__main__':
    sample_value = 2.5
    sample_from = 'hour'
    sample_to = 'minute'
    result_minutes = convert_time(sample_value, sample_from, sample_to)
    print(f"{sample_value} {sample_from} is {result_minutes} {sample_to}")
    
    sample_value_2 = 90
    sample_from_2 = 'minute'
    sample_to_2 = 'hour'
    result_hours = convert_time(sample_value_2, sample_from_2, sample_to_2)
    print(f"{sample_value_2} {sample_from_2} is {result_hours} {sample_to_2}")
    
    sample_value_3 = 1
    sample_from_3 = 'day'
    sample_to_3 = 'second'
    result_seconds = convert_time(sample_value_3, sample_from_3, sample_to_3)
    print(f"{sample_value_3} {sample_from_3} is {result_seconds} {sample_to_3}")
    
    sample_value_4 = 31536000
    sample_from_4 = 'second'
    sample_to_4 = 'year'
    result_years = convert_time(sample_value_4, sample_from_4, sample_to_4)
    print(f"{sample_value_4} {sample_from_4} is {result_years} {sample_to_4}")