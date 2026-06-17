from datetime import datetime
def sort_datetimes_by_date(datetimes):
    return sorted(datetimes, key=lambda dt: dt.date())
if __name__ == '__main__':
    sample_dates = [
        datetime(2023, 10, 27, 14, 30),
        datetime(2023, 10, 25, 9, 0),
        datetime(2023, 10, 28, 10, 0),
        datetime(2023, 10, 27, 10, 0)
    ]
    sorted_dates = sort_datetimes_by_date(sample_dates)
    for dt in sorted_dates:
        print(dt)