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
    
    seconds_per_from_unit = time_units[from_unit]
    seconds_per_to_unit = time_units[to_unit]
    
    value_in_seconds = value * seconds_per_from_unit
    converted_value = value_in_seconds / seconds_per_to_unit
    
    return converted_value

if __name__ == '__main__':
    sample_value_1 = 2
    from_unit_1 = 'day'
    to_unit_1 = 'hour'
    result_1 = convert_time(sample_value_1, from_unit_1, to_unit_1)
    print(f"{sample_value_1} {from_unit_1} is {result_1} {to_unit_1}")

    sample_value_2 = 5
    from_unit_2 = 'week'
    to_unit_2 = 'day'
    result_2 = convert_time(sample_value_2, from_unit_2, to_unit_2)
    print(f"{sample_value_2} {from_unit_2} is {result_2} {to_unit_2}")

    sample_value_3 = 100
    from_unit_3 = 'second'
    to_unit_3 = 'minute'
    result_3 = convert_time(sample_value_3, from_unit_3, to_unit_3)
    print(f"{sample_value_3} {from_unit_3} is {result_3} {to_unit_3}")