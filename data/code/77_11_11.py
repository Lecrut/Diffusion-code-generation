def validate_time_format(time_str):
    parts = time_str.split(':')
    if len(parts) != 3:
        raise ValueError("Incorrect number of time components")
    h, m, s = map(int, parts)
    if not (0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60):
        raise ValueError("Time components out of valid range")

def time_to_minutes(time_str):
    validate_time_format(time_str)
    h, m, s = map(int, time_str.split(':'))
    return h * 60 + m + s / 60

if __name__ == '__main__':
    test_cases = [
        ("00:00:00", 0),
        ("01:30:00", 90),
        ("23:59:59", 1439.9833333333334)
    ]
    for time_str, expected in test_cases:
        result = time_to_minutes(time_str)
        print(f"time_to_minutes('{time_str}') -> {result}, Expected: {expected}")