def time_to_minutes(time_str):
    try:
        hours, minutes, seconds = map(int, time_str.split(':'))
        if hours < 0 or minutes < 0 or seconds < 0:
            raise ValueError("Time components must be non-negative")
        return hours * 60 + minutes + seconds / 60
    except (ValueError, TypeError):
        print("Invalid time format. Please use 'H:M:S'")
        return None

if __name__ == '__main__':
    sample_time = "2:30:45"
    result = time_to_minutes(sample_time)
    if result is not None:
        print(f"Total minutes: {result}")