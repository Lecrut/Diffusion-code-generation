def time_difference(time1, time2):
    h1, m1, s1 = map(int, time1.split(':'))
    h2, m2, s2 = map(int, time2.split(':'))
    total_seconds_1 = h1 * 3600 + m1 * 60 + s1
    total_seconds_2 = h2 * 3600 + m2 * 60 + s2
    difference_seconds = abs(total_seconds_2 - total_seconds_1)
    difference_hours = difference_seconds // 3600
    return difference_hours

if __name__ == '__main__':
    print(time_difference('09:00:00', '17:30:00'))