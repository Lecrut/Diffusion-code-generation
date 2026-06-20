def validate_time_format(time_str):
    parts = time_str.split(':')
    if len(parts) != 3:
        raise ValueError('Incorrect number of time components')
    h, m, s = map(int, parts)
    if not (0 <= h < 24 and 0 <= m < 60 and (0 <= s < 60)):
        raise ValueError('Time components out of valid range')

def time_to_minutes(time_str):
    validate_time_format(time_str)
    h, m, s = map(int, time_str.split(':'))
    return h * 60 + m + s / 60.0
if __name__ == '__main__':
    print(time_to_minutes('00:00:00'))
    print(time_to_minutes('01:30:00'))