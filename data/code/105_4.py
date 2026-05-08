import datetime
def add_days(date_obj, days):
    new_date = date_obj + datetime.timedelta(days=days)
    return new_date
if __name__ == '__main__':
    start_date = datetime.date(2023, 1, 31)
    interval_days = 100
    future_date = add_days(start_date, interval_days)
    print(f"Start Date: {start_date}")
    print(f"Interval: {interval_days} days")
    print(f"Future Date: {future_date}")
    start_date_leap = datetime.date(2024, 2, 28)
    interval_days_leap = 2
    future_date_leap = add_days(start_date_leap, interval_days_leap)
    print(f"Start Date (Leap Year): {start_date_leap}")
    print(f"Interval: {interval_days_leap} days")
    print(f"Future Date (Leap Year): {future_date_leap}")