SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR
WEEK = 7 * DAY
MONTH = 30 * DAY
YEAR = 365 * DAY
TIME_UNITS = {'second': SECOND, 'minute': MINUTE, 'hour': HOUR, 'day': DAY, 'week': WEEK, 'month': MONTH, 'year': YEAR}

def convert_time(value, from_unit, to_unit):
    if from_unit not in TIME_UNITS or to_unit not in TIME_UNITS:
        raise ValueError("Unsupported unit. Please choose from 'second', 'minute', 'hour', 'day', 'week', 'month', 'year'.")
    value_in_seconds = value * TIME_UNITS[from_unit]
    converted_value = value_in_seconds / TIME_UNITS[to_unit]
    return converted_value
if __name__ == '__main__':
    print(convert_time(1, 'hour', 'minute'))
    print(convert_time(7, 'day', 'week'))
    print(convert_time(12, 'month', 'year'))
    print(convert_time(86400, 'second', 'day'))