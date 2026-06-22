def time_difference(time1: str, time2: str) -> str:
    h1, m1 = map(int, time1.split(':'))
    h2, m2 = map(int, time2.split(':'))
    total_minutes = (h2 * 60 + m2) - (h1 * 60 + m1)
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return f"{hours} hour{'s' if hours != 1 else ''}, {minutes} minute{'s' if minutes != 1 else ''}"

if __name__ == '__main__':
    print(time_difference('12:30', '14:45'))