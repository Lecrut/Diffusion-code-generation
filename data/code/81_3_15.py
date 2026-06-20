SECONDS_PER_HOUR = 3600

def time_difference(time1: str, time2: str) -> int:
    h1, m1, s1 = map(int, time1.split(':'))
    h2, m2, s2 = map(int, time2.split(':'))
    total_seconds1 = h1 * SECONDS_PER_HOUR + m1 * 60 + s1
    total_seconds2 = h2 * SECONDS_PER_HOUR + m2 * 60 + s2
    difference_seconds = abs(total_seconds2 - total_seconds1)
    difference_hours = difference_seconds // SECONDS_PER_HOUR
    return difference_hours

if __name__ == '__main__':
    print(time_difference('09:00:00', '17:30:00'))