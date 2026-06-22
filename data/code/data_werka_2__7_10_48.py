SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 3600
SECONDS_PER_DAY = 86400
SECONDS_PER_WEEK = 604800
SECONDS_PER_MONTH = 2592000
SECONDS_PER_YEAR = 31536000
TIME_UNITS = {'second': 1, 'minute': SECONDS_PER_MINUTE, 'hour': SECONDS_PER_HOUR, 'day': SECONDS_PER_DAY, 'week': SECONDS_PER_WEEK, 'month': SECONDS_PER_MONTH, 'year': SECONDS_PER_YEAR}

def convert_time(value, from_unit, to_unit):
    if from_unit not in TIME_UNITS or to_unit not in TIME_UNITS:
        raise ValueError("Unsupported unit. Please choose from 'second', 'minute', 'hour', 'day', 'week', 'month', 'year'.")
    value_in_seconds = value * TIME_UNITS[from_unit]
    converted_value = value_in_seconds / TIME_UNITS[to_unit]
    return converted_value
if __name__ == '__main__':
    print(convert_time(1, 'hour', 'minute'))
    print(convert_time(24, 'day', 'hour'))
    print(convert_time(365, 'year', 'day'))
    print(convert_time(1000, 'second', 'week'))