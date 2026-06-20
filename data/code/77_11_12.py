def time_to_minutes(time_str):
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
        print(f"{time_str} -> {result}, Expected: {expected}")