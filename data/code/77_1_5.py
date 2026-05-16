def time_to_minutes(time_str):
    h, m, s = map(int, time_str.split(':'))
    total_minutes = h * 60 + m + s / 60
    return total_minutes
if __name__ == '__main__':
    test_time1 = "01:30:00"
    result1 = time_to_minutes(test_time1)
    print(f"Time: {test_time1}, Minutes: {result1}")
    test_time2 = "00:05:30"
    result2 = time_to_minutes(test_time2)
    print(f"Time: {test_time2}, Minutes: {result2}")
    test_time3 = "23:59:59"
    result3 = time_to_minutes(test_time3)
    print(f"Time: {test_time3}, Minutes: {result3}")