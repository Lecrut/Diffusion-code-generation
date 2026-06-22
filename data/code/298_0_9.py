def time_difference(time1: str, time2: str) -> int:
    h1, m1 = map(int, time1.split(':'))
    h2, m2 = map(int, time2.split(':'))
    total_minutes1 = h1 * 60 + m1
    total_minutes2 = h2 * 60 + m2
    difference = abs(total_minutes1 - total_minutes2)
    return difference

if __name__ == '__main__':
    sample_time1 = "13:45"
    sample_time2 = "19:00"
    result = time_difference(sample_time1, sample_time2)
    print(result)