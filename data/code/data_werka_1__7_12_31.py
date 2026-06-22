def convert_time(value, from_unit, to_unit):
    time_units = {'second': 1, 'minute': 60, 'hour': 3600, 'day': 86400, 'week': 604800, 'month': 2592000, 'year': 31536000}
    if from_unit not in time_units or to_unit not in time_units:
        raise ValueError('Invalid unit. Supported units are: second, minute, hour, day, week, month, year.')
    value_in_seconds = value * time_units[from_unit]
    converted_value = value_in_seconds / time_units[to_unit]
    return converted_value
if __name__ == '__main__':
    sample_values = [(10, 'minute', 'second'), (2, 'hour', 'minute'), (5, 'day', 'hour'), (365, 'year', 'day')]
    for value, from_unit, to_unit in sample_values:
        result = convert_time(value, from_unit, to_unit)
        print(f'{value} {from_unit}s is equal to {result} {to_unit}s')