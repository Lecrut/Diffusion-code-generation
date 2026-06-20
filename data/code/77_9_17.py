def time_to_minutes(time_str: str) -> float:
    if ':' not in time_str or len(time_str.split(':')) != 3:
        raise ValueError("Invalid time format. Expected 'HH:MM:SS'")
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 60 + minutes + seconds / 60
if __name__ == '__main__':
    try:
        print(time_to_minutes('12:34:56'))
    except ValueError as e:
        print(e)