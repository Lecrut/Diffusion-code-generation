import datetime
def time_to_minutes(time_str):
    try:
        h, m, s = map(int, time_str.split(':'))
        total_seconds = h * 3600 + m * 60 + s
        total_minutes = total_seconds / 60.0
        return total_minutes
    except ValueError:
        raise ValueError("Invalid time format. Expected 'HH:MM:SS'.")
    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    test_times = [
        "00:00:00",
        "23:59:59",
        "01:30:15",
        "9:30:00",
        "invalid_time"
    ]
    for time_str in test_times:
        try:
            minutes = time_to_minutes(time_str)
            print(f"Input: {time_str}, Output: {minutes}")
        except ValueError as e:
            print(f"Input: {time_str}, Error: {e}")
        except Exception as e:
            print(f"Input: {time_str}, Unexpected Error: {e}")