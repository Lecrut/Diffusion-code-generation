def time_to_minutes(time_str):
    try:
        hours, minutes, seconds = map(int, time_str.split(':'))
        return hours * 60 + minutes + seconds / 60
    except (ValueError, AttributeError):
        raise ValueError("Invalid time format. Please use 'HH:MM:SS'.")

if __name__ == '__main__':
    print(time_to_minutes('12:34:56'))
    print(time_to_minutes('00:01:00'))
    print(time_to_minutes('23:59:59'))