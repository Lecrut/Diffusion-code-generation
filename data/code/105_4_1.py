import datetime
def add_days(date_obj, days):
    new_date = date_obj + datetime.timedelta(days=days)
    return new_date
if __name__ == '__main__':
    start_date = datetime.date(2023, 1, 31)
    interval = 30
    future_date = add_days(start_date, interval)
    print(f"Start Date: {start_date}")
    print(f"Interval: {interval} days")
    print(f"Future Date: {future_date}")
    start_date_leap = datetime.date(2024, 2, 28)
    interval_leap = 2
    future_date_leap = add_days(start_date_leap, interval_leap)
    print(f"Start Date: {start_date_leap}")
    print(f"Interval: {interval_leap} days")
    print(f"Future Date: {future_date_leap}")
    start_date_feb_29 = datetime.date(2024, 2, 29)
    interval_feb_29 = 1
    future_date_feb_29 = add_days(start_date_feb_29, interval_feb_29)
    print(f"Start Date: {start_date_feb_29}")
    print(f"Interval: {interval_feb_29} days")
    print(f"Future Date: {future_date_feb_29}")