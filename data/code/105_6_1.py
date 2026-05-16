import datetime
def calculate_nth_day_after(start_date, n):
    if n < 0:
        raise ValueError("N must be a non-negative integer")
    target_date = start_date + datetime.timedelta(days=n)
    return target_date
if __name__ == '__main__':
    start = datetime.date(2023, 10, 26)
    n1 = 7
    result1 = calculate_nth_day_after(start, n1)
    print(f"Start Date: {start}, N: {n1}, Result: {result1}")
    start = datetime.date(2023, 10, 26)
    n2 = 0
    result2 = calculate_nth_day_after(start, n2)
    print(f"Start Date: {start}, N: {n2}, Result: {result2}")
    start = datetime.date(2023, 10, 26)
    n3 = 365
    result3 = calculate_nth_day_after(start, n3)
    print(f"Start Date: {start}, N: {n3}, Result: {result3}")
    start = datetime.date(2023, 10, 26)
    n4 = 1000
    result4 = calculate_nth_day_after(start, n4)
    print(f"Start Date: {start}, N: {n4}, Result: {result4}")