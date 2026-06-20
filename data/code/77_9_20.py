def time_to_minutes(time_str):
    time_map = {'h': 60, 'm': 1}
    parts = time_str.split(':')
    total_minutes = 0.0
    for part in parts:
        value, unit = map(str.strip, part.rsplit(' ', 1))
        if unit not in time_map:
            raise ValueError('Invalid time format')
        total_minutes += float(value) * time_map[unit]
    return total_minutes
if __name__ == '__main__':
    print(time_to_minutes('2:30'))
    print(time_to_minutes('1h30m'))