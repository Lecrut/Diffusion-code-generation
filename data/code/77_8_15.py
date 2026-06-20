def time_to_minutes(time_value):
    if isinstance(time_value, str):
        parts = time_value.replace('h', ':').replace('m', '').split(':')
        hours = int(parts[0])
        minutes = int(parts[1]) if len(parts) > 1 else 0
        return hours * 60 + minutes
    elif isinstance(time_value, (int, float)):
        return time_value * 60
    else:
        raise ValueError('Invalid input type')

if __name__ == '__main__':
    print(time_to_minutes('10:30'))
    print(time_to_minutes('10h30m'))