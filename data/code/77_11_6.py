import datetime
def time_to_minutes(time_str):
    try:
        h, m, s = map(int, time_str.split(':'))
        total_seconds = h * 3600 + m * 60 + s
        total_minutes = total_seconds / 60.0
        return total_minutes
    except ValueError:
        raise ValueError("Invalid time format. Expected HH:MM:SS.")
    except Exception:
        raise ValueError("An unexpected error occurred during time conversion.")
if __name__ == '__main__':
    test_times = [
        "00:00:00",
        "23:59:59",
        "01:30:15",
        "12:00:00"
    ]
    for time_str in test_times:
        try:
            minutes = time_to_minutes(time_str)
            print(f"Input: {time_str}, Output: {minutes}")
        except ValueError as e:
            print(f"Input: {time_str}, Error: {e}")
    invalid_times = [
        "25:00:00",
        "10-30-00",
        "1:2:3"
    ]
    print("\nTesting invalid formats:")
    for time_str in invalid_times:
        try:
            minutes = time_to_minutes(time_str)
            print(f"Input: {time_str}, Output: {minutes}")
        except ValueError as e:
            print(f"Input: {time_str}, Error: {e}")