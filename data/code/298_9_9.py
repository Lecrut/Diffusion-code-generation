def time_difference(time1: str, time2: str) -> int:
    h1, m1 = map(int, time1.split(':'))
    h2, m2 = map(int, time2.split(':'))
    if h1 > h2 or (h1 == h2 and m1 > m2):
        h2 += 24
    return (h2 - h1) * 60 + m2 - m1

if __name__ == '__main__':
    print(time_difference('09:45', '23:15'))
    print(time_difference('23:15', '09:45'))