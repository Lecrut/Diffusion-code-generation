import datetime
def calculate_nth_day_after(start_date, n):
    if n < 0:
        raise ValueError("N must be a non-negative integer")
    target_date = start_date + datetime.timedelta(days=n)
    return target_date
if __name__ == '__main__':
    start_date_str = "2023-10-26"
    n_days = 10
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
    try:
        result_date = calculate_nth_day_after(start_date, n_days)
        print(result_date.strftime("%Y-%m-%d"))
    except ValueError as e:
        print(f"Error: {e}")
    start_date_str_2 = "2023-12-31"
    n_days_2 = 31
    start_date_2 = datetime.datetime.strptime(start_date_str_2, "%Y-%m-%d").date()
    try:
        result_date_2 = calculate_nth_day_after(start_date_2, n_days_2)
        print(result_date_2.strftime("%Y-%m-%d"))
    except ValueError as e:
        print(f"Error: {e}")
    start_date_3 = "2024-01-01"
    n_days_3 = -5
    start_date_3 = datetime.datetime.strptime(start_date_3, "%Y-%m-%d").date()
    try:
        result_date_3 = calculate_nth_day_after(start_date_3, n_days_3)
        print(result_date_3.strftime("%Y-%m-%d"))
    except ValueError as e:
        print(f"Error: {e}")