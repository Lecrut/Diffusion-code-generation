def time_to_minutes(time_str):
    h, m, s = map(int, time_str.split(':'))
    total_seconds = h * 3600 + m * 60 + s
    return total_seconds // 60

if __name__ == '__main__':
    test_times = [
        "00:00:00",
        "23:59:59",
        "01:30:15"
    ]
    for time_str in test_times:
        print(time_to_minutes(time_str))