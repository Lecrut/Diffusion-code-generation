import datetime
def add_days(date_str, days):
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    future_date = date_obj + datetime.timedelta(days=days)
    return future_date.strftime("%Y-%m-%d")
if __name__ == '__main__':
    start_date = "2023-01-31"
    interval = 30
    result = add_days(start_date, interval)
    print(f"Start Date: {start_date}, Interval: {interval} days, Result: {result}")
    start_date_leap = "2024-02-28"
    interval_leap = 2
    result_leap = add_days(start_date_leap, interval_leap)
    print(f"Start Date: {start_date_leap}, Interval: {interval_leap} days, Result: {result_leap}")
    start_date_feb = "2023-02-28"
    interval_feb = 1
    result_feb = add_days(start_date_feb, interval_feb)
    print(f"Start Date: {start_date_feb}, Interval: {interval_feb} days, Result: {result_feb}")