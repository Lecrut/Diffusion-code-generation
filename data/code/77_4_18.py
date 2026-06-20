def convert_to_minutes(duration_str):
    try:
        hours, minutes, seconds = map(int, duration_str.split(':'))
        if hours < 0 or minutes < 0 or seconds < 0:
            raise ValueError("Time components cannot be negative.")
        return (hours * 60) + minutes + (seconds / 60.0)
    except (ValueError, TypeError):
        raise ValueError("Invalid duration format. Expected 'HH:MM:SS'.")

if __name__ == '__main__':
    sample_duration = '1:30:00'
    try:
        total_minutes = convert_to_minutes(sample_duration)
        print(f"Duration: {sample_duration} -> Total minutes: {total_minutes:.2f}")
    except ValueError as e:
        print(e)