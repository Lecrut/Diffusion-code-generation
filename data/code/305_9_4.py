import datetime
if __name__ == '__main__':
    dates = [
        datetime.datetime(2023, 10, 25, 14, 30),
        datetime.datetime(2023, 10, 24, 9, 0),
        datetime.datetime(2023, 10, 26, 10, 0),
        datetime.datetime(2023, 10, 25, 10, 0)
    ]
    sorted_dates = sorted(dates, key=lambda dt: dt.date())
    for dt in sorted_dates:
        print(dt)