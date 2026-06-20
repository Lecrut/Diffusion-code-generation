def time_difference(time1: str, time2: str) -> int:
    h1, m1, s1 = map(int, time1.split(':'))
    h2, m2, s2 = map(int, time2.split(':'))
    return (h2 - h1) + ((m2 - m1) / 60) + ((s2 - s1) / 3600)

if __name__ == '__main__':
    print(time_difference('09:00:00', '17:30:00'))