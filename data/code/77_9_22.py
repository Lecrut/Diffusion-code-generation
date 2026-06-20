def time_to_minutes(time_str):
    try:
        hours, minutes, seconds = map(int, time_str.split(':'))
        return hours * 60 + minutes + seconds / 60.0
    except (ValueError, AttributeError):
        raise ValueError("Invalid time format: expected 'HH:MM:SS'")

if __name__ == '__main__':
    print(time_to_minutes('12:34:56'))