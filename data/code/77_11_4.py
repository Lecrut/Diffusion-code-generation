def time_to_minutes(time_str):
    try:
        h, m, s = map(int, time_str.split(':'))
        total_minutes = h * 60 + m + s / 60
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
            print(f"Input: {time_str}, Result: {result}, Expected: {expected}, Status: {'PASS' if abs(result - expected) < 1e-9 else 'FAIL'}")
        except ValueError as e:
            print(f"Input: {time_str}, Error: {e}, Status: 'ERROR'")
        except Exception as e:
            print(f"Input: {time_str}, Unexpected Error: {e}, Status: 'ERROR'")
    invalid_cases = [
        ("12:30", 1230),
        ("abc:def:ghi", 0),
        ("25:00:00", 0)
    ]
    print("\n--- Testing Invalid Formats ---")
    for time_str in invalid_cases:
        try:
            time_to_minutes(time_str)
            print(f"Input: {time_str}, Status: 'FAIL' (Should have raised an error)")
        except ValueError as e:
            print(f"Input: {time_str}, Caught expected error: {e}, Status: 'PASS'")
        except Exception as e:
            print(f"Input: {time_str}, Caught unexpected error: {e}, Status: 'FAIL'")