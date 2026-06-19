def convert_time(value, from_unit, to_unit):
    time_units = {'seconds': 1, 'minutes': 60, 'hours': 3600, 'days': 86400, 'weeks': 604800, 'months': 2592000, 'years': 31536000}
    if from_unit not in time_units or to_unit not in time_units:
        raise ValueError('Invalid unit. Choose from: seconds, minutes, hours, days, weeks, months, years.')
    value_in_seconds = value * time_units[from_unit]
    converted_value = value_in_seconds / time_units[to_unit]
    return converted_value
if __name__ == '__main__':
    sample_values = [(10, 'minutes', 'seconds'), (2, 'hours', 'minutes'), (5, 'days', 'hours'), (365, 'years', 'days')]
    for value, from_unit, to_unit in sample_values:
        result = convert_time(value, from_unit, to_unit)
        print(f'{value} {from_unit} is equal to {result:.2f} {to_unit}')