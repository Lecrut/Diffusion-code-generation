import re

def time_to_minutes(time_str):
    match = re.match('(\\d+)([h:])(\\d*)', time_str)
    if not match:
        raise ValueError('Invalid time format')
    hours, _, minutes = match.groups()
    return int(hours) * 60 + (int(minutes) if minutes else 0)
if __name__ == '__main__':
    print(time_to_minutes('10:30'))
    print(time_to_minutes('10h30m'))