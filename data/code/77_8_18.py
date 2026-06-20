import re

def time_to_minutes(time_value):
    match = re.match('(\\d+)([h:])(\\d+)?', time_value)
    if not match:
        raise ValueError(f'Invalid time format: {time_value}')
    hours, colon, minutes = match.groups()
    total_minutes = int(hours) * 60
    if minutes is not None:
        total_minutes += int(minutes)
    return total_minutes
if __name__ == '__main__':
    print(time_to_minutes('10:30'))
    print(time_to_minutes('10h30m'))
    print(time_to_minutes('5h'))