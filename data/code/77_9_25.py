def time_to_minutes(time_str):
    time_map = {'h': 60, 'm': 1}
    parts = time_str.lower().split(':')
    if len(parts) == 3:
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])
        return hours * time_map['h'] + minutes + seconds / 60
    elif len(parts) == 2:
        hours = int(parts[0])
        minutes = int(parts[1])
        return hours * time_map['h'] + minutes
    else:
        raise ValueError("Invalid time format")

if __name__ == '__main__':
    print(time_to_minutes('2:30'))
    print(time_to_minutes('1:45:30'))
    try:
        print(time_to_minutes('99:99'))
    except ValueError as e:
        print(e)