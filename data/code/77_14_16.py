def validate_time_format(time_str):
    if not isinstance(time_str, str) or len(time_str) != 5 or time_str[2] != ':':
        raise ValueError('Invalid time format')

def convert_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def calculate_total_minutes(time_str):
    validate_time_format(time_str)
    if not (0 <= int(time_str[:2]) < 24 and 0 <= int(time_str[3:]) < 60):
        raise ValueError('Invalid time range')
    return convert_to_minutes(time_str)

if __name__ == '__main__':
    print(calculate_total_minutes('14:30'))
    print(calculate_total_minutes('23:59'))
    print(calculate_total_minutes('00:00'))