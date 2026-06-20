def time_to_minutes(time_str):
    time_map = {'h': 60, 'm': 1}
    total_minutes = 0
    if ':' in time_str:
        parts = time_str.split(':')
        for part in parts:
            value, unit = (part[:-2], part[-2:])
            if unit in time_map:
                total_minutes += int(value) * time_map[unit]
            else:
                raise ValueError('Invalid time format')
    elif 'h' in time_str or 'm' in time_str:
        for char in time_str:
            if char.isdigit():
                value = value + char
            else:
                unit = char
                total_minutes += int(value) * time_map[unit]
                value = ''
        if value:
            total_minutes += int(value) * time_map[unit]
    else:
        try:
            total_minutes = int(time_str)
        except ValueError:
            raise ValueError('Invalid time format')
    return float(total_minutes)
if __name__ == '__main__':
    print(time_to_minutes('2:30'))
    print(time_to_minutes('1h30m'))
    print(time_to_minutes('90'))