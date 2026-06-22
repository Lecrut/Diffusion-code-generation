def convert_time(value, from_unit, to_unit):
    units = {
        'nanosecond': 1e-9,
        'microsecond': 1e-6,
        'millisecond': 1e-3,
        'second': 1,
        'minute': 60,
        'hour': 3600,
        'day': 86400,
        'week': 604800,
        'month': 2629746,
        'year': 31556952
    }
    
    if from_unit not in units:
        raise ValueError(f"Invalid from_unit: {from_unit}")
    if to_unit not in units:
        raise ValueError(f"Invalid to_unit: {to_unit}")
    
    seconds = value * units[from_unit]
    result = seconds / units[to_unit]
    return result

if __name__ == '__main__':
    sample_input_1 = 60
    sample_from_1 = 'minute'
    sample_to_1 = 'second'
    result_1 = convert_time(sample_input_1, sample_from_1, sample_to_1)
    print(result_1)
    
    sample_input_2 = 3600
    sample_from_2 = 'second'
    sample_to_2 = 'hour'
    result_2 = convert_time(sample_input_2, sample_from_2, sample_to_2)
    print(result_2)
    
    sample_input_3 = 1
    sample_from_3 = 'day'
    sample_to_3 = 'hour'
    result_3 = convert_time(sample_input_3, sample_from_3, sample_to_3)
    print(result_3)