import re

def parse_time_value(time_value):
    if isinstance(time_value, (int, float)):
        return time_value * 60
    elif isinstance(time_value, str):
        match = re.match('(\\d+)([hms]?)', time_value)
        if match:
            value = int(match.group(1))
            unit = match.group(2).lower()
            if unit == 'h':
                return value * 60
            elif unit == 'm':
                return value
            else:
                return value / 60
    raise ValueError('Invalid time format')
if __name__ == '__main__':
    print(parse_time_value('10:30'))
    print(parse_time_value('10h30m'))
    print(parse_time_value(2))
    print(parse_time_value(1.5))