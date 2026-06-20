def parse_time(time_str):
    try:
        hours, minutes, seconds = map(int, time_str.split(':'))
        return hours * 3600 + minutes * 60 + seconds
    except ValueError:
        raise ValueError("Invalid time format. Please use 'HH:MM:SS'.")

def calculate_elapsed_hours(time1, time2):
    total_seconds_time1 = parse_time(time1)
    total_seconds_time2 = parse_time(time2)
    return abs(total_seconds_time1 - total_seconds_time2) / 3600.0

if __name__ == '__main__':
    sample_time1 = '12:34:56'
    sample_time2 = '09:15:30'
    result = calculate_elapsed_hours(sample_time1, sample_time2)
    print(f"Elapsed hours between {sample_time1} and {sample_time2}: {result:.2f}")