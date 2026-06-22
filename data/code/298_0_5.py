def time_difference(time_str1: str, time_str2: str) -> int:
    h1, m1 = map(int, time_str1.split(':'))
    h2, m2 = map(int, time_str2.split(':'))
    total_minutes1 = h1 * 60 + m1
    total_minutes2 = h2 * 60 + m2
    return abs(total_minutes1 - total_minutes2)

if __name__ == '__main__':
    print(time_difference('09:30', '14:45'))