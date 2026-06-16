import datetime
def sort_datetimes_by_date(datetimes):
    return sorted(datetimes, key=lambda dt: dt.date())
if __name__ == '__main__':
    times = [
        datetime.datetime(2023, 10, 26, 14, 30),
        datetime.datetime(2023, 10, 25, 9, 0),
        datetime.datetime(2023, 10, 26, 10, 0),
        datetime.datetime(2023, 10, 27, 18, 45)
    ]
    sorted_times = sort_datetimes_by_date(times)
    for dt in sorted_times:
        print(dt)