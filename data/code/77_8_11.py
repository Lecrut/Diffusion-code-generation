def parse_time(time_value):
    if isinstance(time_value, str):
        time_parts = time_value.replace('h', ':').replace('m', '').split(':')
        hours = int(time_parts[0])
        minutes = int(time_parts[1]) if len(time_parts) > 1 else 0
        return hours * 60 + minutes
    elif isinstance(time_value, (int, float)):
        return time_value * 60
    else:
        raise ValueError('Invalid time format')

def time_to_minutes(time_value):
    return parse_time(time_value)
if __name__ == '__main__':
    print(time_to_minutes('10:30'))
    print(time_to_minutes('10h30m'))
    print(time_to_minutes(1.5))