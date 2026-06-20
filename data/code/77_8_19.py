def parse_time(time_str):
    if 'h' in time_str and 'm' in time_str:
        hours = int(time_str.split('h')[0])
        minutes = int(time_str.split('h')[1].split('m')[0])
        return hours * 60 + minutes
    elif ':' in time_str:
        hours, minutes = map(int, time_str.split(':'))
        return hours * 60 + minutes
    else:
        raise ValueError('Unsupported time format')

def time_to_minutes(time_value):
    if isinstance(time_value, str):
        return parse_time(time_value)
    elif isinstance(time_value, (int, float)):
        return int(time_value * 60)
    else:
        raise TypeError('Invalid input type')
if __name__ == '__main__':
    print(time_to_minutes('10:30'))
    print(time_to_minutes('10h30m'))
    print(time_to_minutes(1.5))