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
    test_cases = [
        ("00:00:00", 0.0),
        ("01:30:00", 90.0),
        ("23:59:59", 1439.9833333333334),
        ("00:01:00", 1.0),
        ("12:00:00", 720.0)
    ]
    for time_str, expected in test_cases:
        try:
            result = time_to_minutes(time_str)
            print(f"Input: {time_str}, Result: {result}, Expected: {expected}, Match: {abs(result - expected) < 1e-9}")
        except ValueError as e:
            print(f"Input: {time_str}, Error: {e}")
        except Exception as e:
            print(f"Input: {time_str}, Unexpected Error: {e}")
    invalid_cases = [
        ("25:00:00", None),
        ("1:2:3", None),
        ("abc", None)
    ]
    print("\nTesting invalid formats:")
    for time_str in invalid_cases:
        try:
            time_to_minutes(time_str)
        except ValueError as e:
            print(f"Input: {time_str}, Caught expected error: {e}")
        except Exception as e:
            print(f"Input: {time_str}, Caught unexpected error: {e}")