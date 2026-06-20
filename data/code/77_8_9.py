def parse_time(time_value):
    if 'h' in time_value and 'm' in time_value:
        hours = int(time_value.split('h')[0])
        minutes = int(time_value.split('h')[1].split('m')[0])
        return hours * 60 + minutes
    elif ':' in time_value:
        parts = time_value.split(':')
        return int(parts[0]) * 60 + int(parts[1])
    else:
        raise ValueError("Unsupported time format")

def time_to_minutes(time_value):
    return parse_time(time_value)

if __name__ == '__main__':
    print(time_to_minutes('10:30'))
    print(time_to_minutes('10h30m'))