import re

def time_to_minutes(time_str):
    match = re.match('(\\d+)([h:])(\\d*)', time_str)
    if not match:
        raise ValueError('Invalid time format')
    hours, sep, minutes = match.groups()
    total_minutes = int(hours) * 60
    if minutes:
        total_minutes += int(minutes)
    return total_minutes
if __name__ == '__main__':
    print(time_to_minutes('10:30'))
    print(time_to_minutes('10h30m'))