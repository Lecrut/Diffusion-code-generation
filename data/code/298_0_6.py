def time_difference(time1: str, time2: str) -> int:
    h1, m1 = map(int, time1.split(':'))
    h2, m2 = map(int, time2.split(':'))
    return ((h2 - h1) * 60 + (m2 - m1)) % 1440
if __name__ == '__main__':
    print(time_difference('12:30', '15:45'))