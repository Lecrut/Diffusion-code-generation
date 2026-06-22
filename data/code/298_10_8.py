def time_diff_minutes(time1: str, time2: str) -> int:
    h1, m1 = map(int, time1.split(':'))
    h2, m2 = map(int, time2.split(':'))
    total_m1 = h1 * 60 + m1
    total_m2 = h2 * 60 + m2
    return abs(total_m2 - total_m1)

if __name__ == '__main__':
    print(time_diff_minutes('14:30', '17:45'))