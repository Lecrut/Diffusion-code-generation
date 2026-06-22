def time_diff_in_minutes(time1, time2):
    h1, m1 = map(int, time1.split(':'))
    h2, m2 = map(int, time2.split(':'))
    total_m1 = h1 * 60 + m1
    total_m2 = h2 * 60 + m2
    return total_m2 - total_m1

if __name__ == '__main__':
    print(time_diff_in_minutes('08:15', '20:45'))
    print(time_diff_in_minutes('20:45', '08:15'))