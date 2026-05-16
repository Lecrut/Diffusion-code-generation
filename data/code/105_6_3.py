import datetime
def nth_day_after(start_date, n):
    if n < 0:
        raise ValueError("N must be a non-negative integer")
    current_date = start_date
    for _ in range(n):
        current_date += datetime.timedelta(days=1)
    return current_date
if __name__ == '__main__':
    start_date_str = "2023-10-26"
    n_days = 10
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
    result_date = nth_day_after(start_date, n_days)
    print(result_date.strftime("%Y-%m-%d"))