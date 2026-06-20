def time_to_minutes(time_value):
    time_map = {'h': 60, 'm': 1}
    if isinstance(time_value, str):
        value, unit = (time_value[:-1], time_value[-1])
        return int(value) * time_map[unit]
    elif isinstance(time_value, (int, float)):
        return int(time_value) * 60
if __name__ == '__main__':
    print(time_to_minutes('10h30m'))
    print(time_to_minutes(1.5))
    print(time_to_minutes(10))