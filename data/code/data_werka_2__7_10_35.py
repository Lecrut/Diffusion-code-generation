def convert_time(value, from_unit, to_unit):
    time_units = {'seconds': 1, 'minutes': 60, 'hours': 3600, 'days': 86400, 'weeks': 604800, 'months': 2592000, 'years': 31536000}
    if from_unit not in time_units or to_unit not in time_units:
        raise ValueError('Unsupported unit')
    value_in_seconds = value * time_units[from_unit]
    converted_value = value_in_seconds / time_units[to_unit]
    return converted_value
if __name__ == '__main__':
    print(convert_time(1, 'hour', 'minutes'))
    print(convert_time(2, 'days', 'hours'))
    print(convert_time(3, 'weeks', 'seconds'))