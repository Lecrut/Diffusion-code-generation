def time_diff_ms(time1: str, time2: str) -> int:
    h1, m1, s1 = map(int, time1.split(':'))
    h2, m2, s2 = map(int, time2.split(':'))
    total_s1 = h1 * 3600 + m1 * 60 + s1
    total_s2 = h2 * 3600 + m2 * 60 + s2
    return abs((total_s2 - total_s1) * 1000)

if __name__ == '__main__':
    print(time_diff_ms('12:34:56', '12:35:07'))