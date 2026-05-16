import datetime
def nth_day_after(start_date, n):
    if n <= 0:
        raise ValueError("N must be a positive integer")
    target_date = start_date + datetime.timedelta(days=n)
    return target_date
if __name__ == '__main__':
    start_date_str = "2023-10-26"
    n_value = 10
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
    try:
        result_date = nth_day_after(start_date, n_value)
        print(result_date.strftime("%Y-%m-%d"))
    except ValueError as e:
        print(f"Error: {e}")