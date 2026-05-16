import datetime
def find_nth_day_after(start_date, n):
    if n < 0:
        raise ValueError("N must be a non-negative integer")
    target_date = start_date + datetime.timedelta(days=n)
    return target_date
if __name__ == '__main__':
    start = datetime.date(2023, 10, 26)
    n1 = 7
    result1 = find_nth_day_after(start, n1)
    print(f"Start Date: {start}, N: {n1}, Result: {result1}")
    start = datetime.date(2023, 1, 1)
    n2 = 365
    result2 = find_nth_day_after(start, n2)
    print(f"Start Date: {start}, N: {n2}, Result: {result2}")
    start = datetime.date(2023, 12, 31)
    n3 = 1
    result3 = find_nth_day_after(start, n3)
    print(f"Start Date: {start}, N: {n3}, Result: {result3}")
    start = datetime.date(2023, 1, 1)
    n4 = 0
    result4 = find_nth_day_after(start, n4)
    print(f"Start Date: {start}, N: {n4}, Result: {result4}")
    try:
        find_nth_day_after(start, -1)
    except ValueError as e:
        print(f"Error caught: {e}")