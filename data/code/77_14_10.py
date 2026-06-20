def time_to_minutes(time_str):
    if not isinstance(time_str, str) or len(time_str) != 5 or time_str[2] != ':':
        raise ValueError('Invalid time format')
    try:
        hours, minutes = map(int, time_str.split(':'))
    except ValueError:
        raise ValueError('Invalid time format') from None
    if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
        raise ValueError('Invalid time range')
    return hours * 60 + minutes

if __name__ == '__main__':
    print(time_to_minutes('14:30'))
    print(time_to_minutes('23:59'))
    print(time_to_minutes('00:00'))