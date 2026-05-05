def time_to_minutes(time_str):
    h, m, s = map(int, time_str.split(':'))
    total_minutes = h * 60 + m + s / 60
    return total_minutes
if __name__ == '__main__':
    time1 = "00:00:00"
    print(time_to_minutes(time1))
    time2 = "01:30:00"
    print(time_to_minutes(time2))
    time3 = "23:59:59"
    print(time_to_minutes(time3))
    time4 = "00:01:00"
    print(time_to_minutes(time4))