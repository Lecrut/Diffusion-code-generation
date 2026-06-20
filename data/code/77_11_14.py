def time_to_minutes(time_str):
    h, m, s = map(int, time_str.split(':'))
    total_minutes = h * 60 + m + s / 60.0
    return int(total_minutes)

if __name__ == '__main__':
    test_times = [
        "00:00:00",
        "23:59:59",
        "01:30:15",
        "99:99:99"
    ]
    
    for time_str in test_times:
        print(time_to_minutes(time_str))