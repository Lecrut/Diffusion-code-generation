def calculate_time_difference(time_str1: str, time_str2: str) -> int:
    h1, m1 = map(int, time_str1.split(':'))
    h2, m2 = map(int, time_str2.split(':'))
    total_minutes1 = h1 * 60 + m1
    total_minutes2 = h2 * 60 + m2
    return abs(total_minutes1 - total_minutes2)

if __name__ == '__main__':
    t1 = "09:30"
    t2 = "14:45"
    result = calculate_time_difference(t1, t2)
    print(result)