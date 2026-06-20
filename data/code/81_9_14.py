def calculate_elapsed_hours(time_str1, time_str2):
    try:
        h1, m1, s1 = map(int, time_str1.split(':'))
        h2, m2, s2 = map(int, time_str2.split(':'))
        total_seconds1 = h1 * 3600 + m1 * 60 + s1
        total_seconds2 = h2 * 3600 + m2 * 60 + s2
        elapsed_seconds = abs(total_seconds1 - total_seconds2)
        return elapsed_seconds / 3600.0
    except ValueError:
        return None

if __name__ == '__main__':
    print(calculate_elapsed_hours('12:34:56', '09:12:34'))