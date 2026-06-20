import re

def time_to_minutes(time_value):
    match = re.match('(\\d+)(h|m)?', time_value)
    if not match:
        raise ValueError('Invalid time format')
    hours, minutes = (0, 0)
    value_str, unit = match.groups()
    value = int(value_str)
    if unit == 'h':
        hours = value
    elif unit == 'm':
        minutes = value
    else:
        hours = value // 100
        minutes = value % 100
    return hours * 60 + minutes
if __name__ == '__main__':
    try:
        print(time_to_minutes('10:30'))
        print(time_to_minutes('10h30m'))
        print(time_to_minutes('5'))
    except ValueError as e:
        print(e)