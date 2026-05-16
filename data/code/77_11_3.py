import datetime
def time_to_minutes(time_str):
    try:
        h, m, s = map(int, time_str.split(':'))
        total_seconds = h * 3600 + m * 60 + s
        total_minutes = total_seconds / 60.0
        return total_minutes
    except ValueError:
        raise ValueError("Invalid time format. Expected 'HH:MM:SS'.")
    except Exception:
        raise ValueError("An unexpected error occurred during time conversion.")
if __name__ == '__main__':
    test_times = [
        "00:00:00",
        "23:59:59",
        "01:30:15",
        "99:99:99",
        "10-20-30",
        "1:2:3"
    ]
    for time_str in test_times:
        try:
            minutes = time_to_minutes(time_str)
            print(f"Input: {time_str}, Result: {minutes}")
        except ValueError as e:
            print(f"Input: {time_str}, Error: {e}")
        except Exception as e:
            print(f"Input: {time_str}, Unexpected Error: {e}")