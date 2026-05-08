import datetime
def find_nth_day_after(start_date, n):
    target_date = start_date + datetime.timedelta(days=n)
    return target_date
if __name__ == '__main__':
    start_date_str = "2023-10-26"
    n_days = 10
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
    result_date = find_nth_day_after(start_date, n_days)
    print(result_date.strftime("%Y-%m-%d"))