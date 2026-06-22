def time_difference(time1: str, time2: str) -> int:
    h1, m1 = map(int, time1.split(':'))
    h2, m2 = map(int, time2.split(':'))
    total_minutes1 = h1 * 60 + m1
    total_minutes2 = h2 * 60 + m2
    return abs(total_minutes2 - total_minutes1)
if __name__ == '__main__':
    print(time_difference('14:30', '19:45'))