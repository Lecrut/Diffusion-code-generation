def time_to_minutes(time_str):
    try:
        parts = time_str.split(':')
        if len(parts) != 3:
            raise ValueError("Incorrect number of time components")
        h = int(parts[0])
        m = int(parts[1])
        s = int(parts[2])
        if not (0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59):
            raise ValueError("Time components out of valid range")
        total_minutes = h * 60 + m + s
        return float(total_minutes)
    except ValueError:
        raise ValueError("Invalid time format. Expected HH:MM:SS")
if __name__ == '__main__':
    test_cases = [
        ("00:00:00", 0.0),
        ("00:01:00", 1.0),
        ("01:00:00", 60.0),
        ("23:59:59", 1439.99),
        ("12:30:15", 750.25)
    ]
    error_cases = [
        ("25:00:00", "Invalid hour"),
        ("10:70:00", "Invalid minute"),
        ("10:30", "Incorrect format"),
        ("abc:def:ghi", "Invalid characters")
    ]
    print("--- Valid Tests ---")
    for time_str, expected in test_cases:
        try:
            result = time_to_minutes(time_str)
            print(f"Input: {time_str}, Result: {result}, Expected: {expected}, Status: {'PASS' if abs(result - expected) < 1e-9 else 'FAIL'}")
        except ValueError as e:
            print(f"Input: {time_str}, Error: {e}, Status: FAIL")
    print("\n--- Error Handling Tests ---")
    for time_str, error_type in error_cases:
        try:
            time_to_minutes(time_str)
            print(f"Input: {time_str}, Expected Error, Status: FAIL")
        except ValueError as e:
            print(f"Input: {time_str}, Caught Expected Error: {e}, Status: PASS")
        except Exception as e:
            print(f"Input: {time_str}, Caught Unexpected Error: {e}, Status: FAIL")