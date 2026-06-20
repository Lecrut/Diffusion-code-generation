def time_to_minutes(time_str):
    try:
        hours, minutes, seconds = map(int, time_str.split(':'))
        total_minutes = hours * 60 + minutes + seconds / 60
        return total_minutes
    except ValueError:
        raise ValueError("Invalid time format. Please use 'HH:MM:SS'.")

if __name__ == '__main__':
    sample_time = "01:30:45"
    try:
        result = time_to_minutes(sample_time)
        print(result)
    except ValueError as e:
        print(e)