def convert_time(value, from_unit, to_unit):
    SECONDS_IN_MINUTE = 60
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_DAY = 86400
    SECONDS_IN_WEEK = 604800
    SECONDS_IN_MONTH = 2592000
    SECONDS_IN_YEAR = 31536000
    time_units = {'second': 1, 'minute': SECONDS_IN_MINUTE, 'hour': SECONDS_IN_HOUR, 'day': SECONDS_IN_DAY, 'week': SECONDS_IN_WEEK, 'month': SECONDS_IN_MONTH, 'year': SECONDS_IN_YEAR}
    if from_unit not in time_units or to_unit not in time_units:
        raise ValueError("Unsupported unit. Please choose from 'second', 'minute', 'hour', 'day', 'week', 'month', 'year'.")
    value_in_seconds = value * time_units[from_unit]
    converted_value = value_in_seconds / time_units[to_unit]
    return converted_value
if __name__ == '__main__':
    print(convert_time(1, 'hour', 'minute'))
    print(convert_time(7, 'day', 'week'))
    print(convert_time(12, 'month', 'year'))
    print(convert_time(3600, 'second', 'hour'))